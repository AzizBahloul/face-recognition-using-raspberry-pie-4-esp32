
# Employee Presence Detection System / Smart Lock

This project implements an advanced presence detection and smart lock system using Arduino, ESP32 with a camera, and Raspberry Pi. It is designed for applications such as employee attendance tracking and sophisticated smart lock solutions.

## Repository Structure

- **`Arduino/`**: Arduino-related files
  - **`ESP32CAM-FIREBASE/`**: Integration of ESP32 camera with Firebase
- **`esp32 board/`**: ESP32-specific code
- **`raspberry_pi/`**: Raspberry Pi code and resources
  - **`dataset/`**: Training data for facial recognition
  - **`facial_req.py`**: Main facial recognition script
  - **`train_model.py`**: Script for training the facial recognition model
  - Other supporting files for the facial recognition system

## Features

- Facial recognition for employee identification
- Integration with Firebase for data storage and management
- ESP32 camera module for image capture
- Potential for remote access and control

## Setup and Installation

### 1. Arduino and ESP32 Setup

- Follow the [instructions for setting up the Arduino IDE and ESP32](#).
- Flash the `ESP32CAM-FIREBASE.ino` file to the ESP32.

### 2. Raspberry Pi Setup

- Refer to the [instructions for setting up the Raspberry Pi](#).
- Install the required libraries using the following command:
  ```sh
  pip install -r requirements.txt
  ```

### 3. Facial Recognition Model

- Place employee images in the `dataset/` directory.
- Run the following command to create the facial recognition model:
  ```sh
  python train_model.py
  ```

### 4. Firebase Configuration

- Set up a Firebase project [here](https://firebase.google.com/).
- Update the `credentials.json` file with your Firebase credentials.

## Usage

1. Start the facial recognition system by executing:
   ```sh
   python facial_req.py
   ```
2. Follow the instructions for configuring and running the ESP32 and Raspberry Pi components.

## Dependencies

- **Python Libraries**:
  - `face_recognition`
  - `firebase_admin`
  - `opencv-python`
  - `paho-mqtt`
  - `paramiko`
- **Arduino IDE**
- **Firebase Account**

## Contributing

Contributions are welcome. Please follow the standard open-source guidelines for contributing.

## License

This project is licensed under the [MIT License](LICENSE). See the LICENSE file for details.

