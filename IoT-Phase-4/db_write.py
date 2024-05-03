import sqlite3
import MQTT_Sub as mqtt_sub
import time
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'Phase04.db')

mqtt_sub.start_mqtt_client()

def get_user_by_rfid():
    rfid_data = mqtt_sub.get_rfid_data()
    print(f"RFID data received: {rfid_data}")
    if not rfid_data:
        return None
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute('SELECT Name FROM UserThresholds WHERE RFID = ?', (rfid_data,))
    user = cursor.fetchone()
    conn.close()
    return user[0] if user else None

try:
    while True:
        user = get_user_by_rfid()
        if user:
            print(f"User with RFID {mqtt_sub.get_rfid_data()} found: {user}")
        else:
            print(f"No user found with RFID {mqtt_sub.get_rfid_data()}")
        time.sleep(1)
except KeyboardInterrupt:
    print("Process stopped by user")
