import paho.mqtt.client as mqtt

# Variables to store LED status and light brightness
led_status = ''
light_brightness = ''

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("light-sensor/brightness")
    client.subscribe("led/status")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global led_status, light_brightness
    if msg.topic == "light-sensor/brightness":
        light_brightness = msg.payload.decode()
        # print(light_brightness)
    elif msg.topic == "led/status":
        led_status = msg.payload.decode()
        # print(led_status)

def start_mqtt_client():
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.on_connect = on_connect
    mqttc.on_message = on_message

    mqttc.connect("192.168.241.68", 1883, 60)

    # Start the MQTT client loop in a separate thread
    mqttc.loop_start()

def get_led_status():
    global led_status
    return led_status

def get_light_brightness():
    global light_brightness
    return light_brightness
