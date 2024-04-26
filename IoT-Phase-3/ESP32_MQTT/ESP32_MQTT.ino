#include <WiFi.h>
#include <PubSubClient.h>

// WiFi credentials
const char* ssid = "";
const char* password = "";

// MQTT broker details
const char* mqtt_server = "192.168.33.68";
const int mqtt_port = 1883; // default MQTT port

// Initialize the WiFi client object
WiFiClient espClient;

// Initialize the MQTT client object
PubSubClient client(espClient);

// MQTT topics
const char* lightsensor_topic = "light-sensor/brightness";
const char* led_status_topic = "led/status";

// Pin connected to the photoresistor
const int photoresistorPin = 34; // Example pin, change to your pin number

// Pin connected to the LED
const int ledPin = 13; // Example pin, change to your pin number

void setup_wifi() {
  delay(10);
  // Connect to Wi-Fi network
  Serial.println();
  Serial.print("Connecting to ");
  Serial.println(ssid);

  WiFi.begin(ssid, password);

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("");
  Serial.println("WiFi connected");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
}

void reconnect() {
  // Loop until we're reconnected
  while (!client.connected()) {
    Serial.print("Attempting MQTT connection...");
    // Attempt to connect
    if (client.connect("ESP32Client")) {
      Serial.println("connected");
    } else {
      Serial.print("failed, rc=");
      Serial.print(client.state());
      Serial.println(" try again in 5 seconds");
      // Wait 5 seconds before retrying
      delay(5000);
    }
  }
}

void setup() {
  Serial.begin(115200);
  setup_wifi();
  client.setServer(mqtt_server, mqtt_port);
  pinMode(photoresistorPin, INPUT);
  pinMode(ledPin, OUTPUT);
}

void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();

  // Read the value from the photoresistor
  int sensorValue = analogRead(photoresistorPin);

  // Convert sensor value to brightness level (0-100)
  int brightness = map(sensorValue, 0, 4095, 0, 1000);
  
  // Print the sensor value to Serial Monitor
  Serial.print("Sensor Value: ");
  Serial.println(brightness);
  
  // Publish brightness level to MQTT topic
  String lightMessage = String(brightness);
//  client.publish(lightsensor_topic, lightMessage.c_str());
  
  // Publish value for LED
  String statusLed = "";

  // Control the LED based on the brightness level
  if (brightness < 400) {
    digitalWrite(ledPin, HIGH);
    statusLed = "LED ON";
  } else {
    digitalWrite(ledPin, LOW);
    statusLed = "LED OFF";
  }

  Serial.print("LED Status: ");
  Serial.println(statusLed);
//  delay(1500);

  // Publish a message every 5 seconds
//  static unsigned long lastMillis = 0;
//  if (millis() - lastMillis > 5000) {
//    lastMillis = millis();
    // Example message to publish
//    String message = "Hello, MQTT!";
    client.publish(lightsensor_topic, lightMessage.c_str());
    client.publish(led_status_topic, statusLed.c_str());
//  }
}
