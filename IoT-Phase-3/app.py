from dash import Dash, html, dcc, Output, Input
import email_system as notification_email
import MQTT_Sub as mqtt_sub
from datetime import datetime, timedelta

# Define a variable to store the time when the last email was sent
last_email_time = None
# Define the minimum time interval between emails (in seconds)
email_interval = 60  # Adjust this value as needed

app = Dash(__name__)

app.layout = html.Div([
    html.H1(
        id='Title',
        children='Phase 3',
        style={'textAlign': 'center'}
    ),
    html.Img(
        id='led',
        src='assets/LED OFF.jpg',  # image path
        alt='LED light',
        style={'display': 'block', 'margin': 'auto'}
    ),
    dcc.Slider(
        id="light-sensor-slider",
        min=0,
        max=1000,
        value=0,
        disabled=True,
    ),
    html.H1(
        id='email-status',
        children='',
        style={'textAlign': 'center'}
    ),
    dcc.Interval(
        id='interval-component',
        interval=500,
        n_intervals=0
    )
])

# Start the MQTT client when the Dash app starts
mqtt_sub.start_mqtt_client()


# Callback to update Dash app layout with MQTT data
@app.callback(
    [Output('led', 'src'),
     Output('light-sensor-slider', 'value')],
    Input('interval-component', 'n_intervals')  # Using an interval component to trigger updates
)
def update_mqtt_data(n):
    global last_email_time  # Use global variable for tracking last email time
    print(mqtt_sub.get_led_status(), mqtt_sub.get_light_brightness())
    if  mqtt_sub.get_led_status() == 'LED ON':
        if last_email_time is None or datetime.now() - last_email_time >= timedelta(seconds=email_interval):
            notification_email.send_email()
            last_email_time = datetime.now()
    return [f"assets/{mqtt_sub.get_led_status()}.jpg", int(mqtt_sub.get_light_brightness())]


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='192.168.241.68', port=8050, debug=True)
