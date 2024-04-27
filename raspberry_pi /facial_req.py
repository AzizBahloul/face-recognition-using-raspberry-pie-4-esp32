import firebase_admin
from firebase_admin import credentials, storage
import face_recognition
import pickle
import cv2
import numpy as np
import paho.mqtt.publish as publish
import time

# Initialize Firebase Admin SDK
cred = credentials.Certificate("credentials.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'ousema1-19138.appspot.com'})

# Determine faces from encodings.pickle file model created from train_model.py
encodingsP = "encodings.pickle"

# Load the known faces and embeddings
print("[INFO] loading encodings + face detector...")
data = pickle.loads(open(encodingsP, "rb").read())

# Specify the directory path within Firebase Storage
directory_path = "newphoto/"

# Set the number of iterations
num_iterations = 100

# Set the time interval to 30 seconds
verification_interval = 30

# Function to send data to ESP32 using MQTT
def send_to_esp32(topic, message):
    # Update the MQTT broker address and other parameters as needed
    mqtt_broker = "broker.hivemq.com"
    mqtt_port = 1883
    publish.single(topic, message, hostname=mqtt_broker, port=mqtt_port)

for iteration in range(1, num_iterations + 1):
    # Get the list of files in the "newphoto" folder
    blobs = list(storage.bucket().list_blobs(prefix=directory_path))

    # Check if there are any new files in the "newphoto" folder
    if blobs:
        for blob in blobs:
            if not blob.name.endswith('/'):
                image_file_name = blob.name[len(directory_path):]

                print(f"Downloading image: {directory_path}{image_file_name}")
                image_bytes = blob.download_as_bytes()

                # Detect the face boxes
                input_image = cv2.imdecode(np.frombuffer(image_bytes, np.uint8), -1)
                boxes = face_recognition.face_locations(input_image)
                encodings = face_recognition.face_encodings(input_image, boxes)
                names = []

                # Loop over the facial embeddings
                for encoding in encodings:
                    # Attempt to match each face in the input image to our known encodings
                    matches = face_recognition.compare_faces(data["encodings"], encoding)
                    name = "Unknown"  # If face is not recognized, then print Unknown

                    # Check to see if we have found a match
                    if True in matches:
                        # Find the indexes of all matched faces then initialize a
                        # dictionary to count the total number of times each face
                        # was matched
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}

                        # Loop over the matched indexes and maintain a count for
                        # each recognized face
                        for i in matchedIdxs:
                            name = data["names"][i]
                            counts[name] = counts.get(name, 0) + 1

                        # Determine the recognized face with the largest number
                        # of votes (note: in the event of an unlikely tie, Python
                        # will select the first entry in the dictionary)
                        name = max(counts, key=counts.get)

                    # Update the list of names
                    names.append(name)

                # Print the recognized face names to the terminal outside of the loop
                print("\nRecognized faces:")
                recognized_names = []

                for name in names:
                    print(name)
                    recognized_names.append(name)

                # Publish the recognized face names to the MQTT topic
                for name in recognized_names:
                    if name != "Unknown":
                        topic = "facial_recognition_results"
                        message = f"Recognized face: {name}"
                        publish.single(topic, message, hostname="broker.hivemq.com")

                        # Send the recognized face name to ESP32
                        send_to_esp32(topic, message)

                # Upload the recognized face to the Firebase folder named after the person's name
                for name in recognized_names:
                    if name != "Unknown":
                        # Create a folder with the person's name in Firebase Storage
                        folder_name = "/" + name + "/"
                        blob_name = folder_name + image_file_name
                        blob = storage.bucket().blob(blob_name)

                        # Upload the new recognized face to the Firebase folder
                        with blob.open("wb") as f:
                            f.write(image_bytes)

                        # Write the recognized name to a text file inside the folder
                        txt_blob_name = folder_name + f"{name}_recognized.txt"
                        txt_blob = storage.bucket().blob(txt_blob_name)
                        with txt_blob.open("w") as txt_file:
                            txt_file.write(name)

        # Sleep for the specified interval before the next iteration
        if iteration < num_iterations:
            print(f"\nWaiting for {verification_interval} seconds before the next iteration...\n")
            time.sleep(verification_interval)

# End of the program
print("\nFace verification completed.")

