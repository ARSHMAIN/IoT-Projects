'''
IoT Project Phase03
Maximus Taube
2095310
UI design and implementation with database.
'''

import sqlite3
import os
import dash
from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
import email_system as notification_email
import MQTT_Sub as mqtt_sub
from datetime import datetime, timedelta

last_email_time = None
email_interval = 60  # Adjust this value as needed

app = Dash(__name__)

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

# Get the current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(current_dir, 'Phase03.db')

# Connect to the SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get the user names and RFID from the database
cursor.execute('SELECT Name, RFID FROM UserThresholds')
user_rows = cursor.fetchall()
user_options = [{'label': user[0], 'value': user[1]} for user in user_rows]

# Close the database connection
conn.close()

# Rest of the code remains the same
app = dash.Dash(__name__)

# IoT dashboard layout
dashboard_layout = html.Div([
    html.H1(
        id='Title',
        children='Phase 3',
        style={'textAlign': 'center', 'font-family': 'Helvetica Neue', 'font-weight': 'bold'}
    ),
    html.Div(
        className='container',  
        style={'textAlign': 'center'},  
        children=[
            html.Div(
                id='light-status-text',
                children='Light Status',
                style={'color': 'black', 'font-size': '24px', 'font-family': 'Helvetica Neue', 'font-weight': 'bold'}
            ),
            html.Img(
                id='led',
                src='assets/LED OFF.jpg', 
                alt='LED light',
                style={'display': 'block', 'margin': 'auto'}
            ),
        ]
    ),
    html.Div(
        className='container',  
        style={'textAlign': 'center'},  
        children=[
            html.Div(
                id='light-intensity-text',
                children=['Light Intensity: ', html.Span(id='light-intensity-value', children="Placeholder")],
                style={'color': 'black', 'font-size': '24px', 'font-family': 'Helvetica Neue', 'font-weight': 'bold'}
            ),
            html.Div(
                dcc.Slider(
                    id="light-sensor-slider",
                    min=0,
                    max=1000,
                    value=0,
                    disabled=True,
                ),
                style={'padding': '20px'}
            ),
        ]
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

def email_message(light_value):
    if light_value > 400:
        return "Email has been sent"
    else:
        return ""
    
# Start the MQTT client when the Dash app starts
mqtt_sub.start_mqtt_client()


# Callback to update Dash app layout with MQTT data
@app.callback(
    [Output('led', 'src'),
     Output('light-sensor-slider', 'value'),
     Output('email-status', 'children'),
     Output('light-intensity-value', 'children')],  # Add Output for light intensity value
    Input('interval-component', 'n_intervals')  # Using an interval component to trigger updates
)
def update_mqtt_data(n):
    global last_email_time  # Use global variable for tracking last email time
    if mqtt_sub.get_led_status() == 'LED ON':
        if last_email_time is None or datetime.now() - last_email_time >= timedelta(seconds=email_interval):
            notification_email.send_email()
            last_email_time = datetime.now()
    light_value = int(mqtt_sub.get_light_brightness())
    email_status = email_message(light_value)  # Call email_message function
    return f"assets/{mqtt_sub.get_led_status()}.jpg", light_value, email_status, light_value

# App layout with login page
app.layout = html.Div([
    html.H1("Login"),
    html.Label("Select User"),
    dcc.Dropdown(id='user-dropdown', options=user_options, value=None),
    html.Label("RFID"),
    dcc.Input(id='password-input', type='text', value=''),
    html.Button('Login', id='login-button', n_clicks=0),
    html.Div(id='login-message'),
    html.Div(id='page-content')
])

# Callback to handle login and redirect to dashboard if successful
@app.callback(
    Output('page-content', 'children'),
    Output('login-message', 'children'),
    Input('login-button', 'n_clicks'),
    State('user-dropdown', 'value'),
    State('password-input', 'value')
)
def login(n_clicks, selected_user, password):
    if n_clicks > 0:
        if selected_user and password == selected_user:  # Compare with RFID
            # Redirect to the IoT dashboard page
            return dashboard_layout, ''
        else:
            return '', html.Div("Invalid user or password")
    else:
        return '', ''

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)