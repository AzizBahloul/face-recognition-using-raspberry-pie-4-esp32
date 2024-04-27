#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <WiFi.h>
#include <PubSubClient.h>

// Replace with your WiFi credentials
const char* ssid = "ssid";
const char* password = "password";

// Replace with your MQTT broker address
const char* mqtt_server = "broker.hivemq.com";

// Replace with the MQTT topic you are subscribing to
const char* topic = "facial_recognition_results";

// Replace with the I2C address of your OLED display
#define OLED_ADDR   0x3C

Adafruit_SSD1306 display(128, 64, &Wire, -1);

WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  Serial.begin(115200);

  // Connect to Wi-Fi
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting to WiFi...");
  }
  Serial.println("Connected to WiFi");

  // Set up OLED display
  if(!display.begin(OLED_ADDR)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;);
  }
  display.display();
  delay(2000);  // Pause for 2 seconds

  // Clear the display
  display.clearDisplay();
  display.display();

  // Set up MQTT client
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
}

void callback(char* received_topic, byte* payload, unsigned int length) {
  Serial.println("Message received from MQTT broker:");

  // Create a buffer to hold the payload and convert it to a string
  char payloadString[length + 1];
  memcpy(payloadString, payload, length);
  payloadString[length] = '\0';

  Serial.print("Topic: ");
  Serial.println(received_topic);
  Serial.print("Payload: ");
  Serial.println(payloadString);

  // Display the name on OLED
  display.clearDisplay();
  display.setTextSize(1);
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(0, 0);
  display.println("Recognized face:");
  display.println(payloadString);
  display.display();
}

void reconnect() {
  // Loop until we're reconnected to the MQTT broker
  while (!client.connected()) {
    Serial.println("Attempting MQTT connection...");
    if (client.connect("ESP32Client")) {
      Serial.println("Connected to MQTT broker");
      // Subscribe to the topic
      client.subscribe(topic);
    } else {
      Serial.print("Failed, rc=");
      Serial.print(client.state());
      Serial.println(" Retrying in 5 seconds...");
      delay(5000);
    }
  }
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }

  // Check for incoming MQTT messages
  client.loop();
}
