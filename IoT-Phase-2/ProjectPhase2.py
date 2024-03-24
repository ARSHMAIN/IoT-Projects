import dash_daq as daq
from dash import Dash, html, Input, Output, callback
import RPi.GPIO as GPIO
import Freenove_DHT as DHT
import time

DHTPin = 11

app = Dash(__name__)

GPIO.setmode(GPIO.BCM)
LED_PIN = 17
GPIO.setup(LED_PIN, GPIO.OUT)

app.layout = html.Div([
    html.Div(
        'IoT Phase 2 Project',
        style={'text-align': 'center', 'margin': '10px'}
    ),
    daq.ToggleSwitch(
        id='email-switch',
        value=False,  
    ),
    html.Div(
        id='email-state',
        style={'text-align': 'center', 'margin-top': '20px'}
    ),
    daq.Thermometer(
        id='thermometer',
        label='Current Temperature',
        labelPosition='top',
        showCurrentValue=True,
        units="C",
        value=6,
        min=-30,
        max=30,
        style={'margin-bottom': '5%'}
    ),
    html.Img(
        id='fan',
        src='assets/fan on.png', 
        alt='Fan',
        style={'display': 'block', 'margin': 'auto'}
    ),
    daq.Gauge(
        color={"gradient": True, "ranges": {"green": [0, 18], "yellow": [18, 24], "red": [24, 30]}},
        id='gauge',
        label="Humidity",
        value=6,
        max=30,
        min=0,
    ),
])

@app.callback(Output('gauge', 'value'), [])
def update_gauge_value():
    dht = DHT.DHT(DHTPin)  
    counts = 0
    while True:
        counts += 1
        print("Measurement counts: ", counts)
        for i in range(0, 15):
            chk = dht.readDHT11()
            if chk is dht.DHTLIB_OK:
                print("DHT11, OK!")
                return dht.temperature  
            time.sleep(0.1)
        print("Failed to read DHT11 data")
        time.sleep(2)

@app.callback(
    [Output('email-state', 'children'),
     Output('email-switch', 'color'),
     Output('fan', 'src')],
    [Input('email-switch', 'value')]
)
def update_output(value):
    if value:
        GPIO.output(LED_PIN, GPIO.HIGH)
        print('Turn ON on.')
        return 'Turn ON on.', 'blue', 'assets/fan on.png' 
    else:
        GPIO.output(LED_PIN, GPIO.LOW)
        print('Turn OFF fan.')
        return 'Turn OFF fan.', 'none', 'assets/fan off.png'  

if __name__ == '__main__':
    app.run_server(debug=True)
