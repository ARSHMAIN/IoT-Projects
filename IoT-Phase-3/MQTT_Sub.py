import paho.mqtt.client as mqtt

led_status = ''
light_brightness = ''

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    client.subscribe("light-sensor/brightness")
    client.subscribe("led/status")

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

    mqttc.connect("192.168.33.68", 1883, 60)

    mqttc.loop_start()

def get_led_status():
    global led_status
    return led_status

def get_light_brightness():
    global light_brightness
    return light_brightness
