'''
IoT Project Phase03
Maximus Taube
2095310
UI design and implementation with database.
'''

import sqlite3
import os
import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

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
    html.H1("IoT Dashboard"),
    # Add your IoT dashboard components here
])

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
