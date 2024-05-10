import dash
from dash import html, dcc
from dynamic import navbar
import dash_daq as daq
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP, dbc.icons.FONT_AWESOME])

app.layout = html.Div([
    dbc.NavbarSimple([
        dbc.NavItem([
            dbc.Label(className="fa fa-moon", html_for="switch"),
            dbc.Switch(id="switch", value=True, className="d-inline-block ms-1", persistence=True),
            dbc.Label(className="fa fa-sun", html_for="switch"),
        ], style={"color": "white"}
        )
    ],
        brand="Smart Home System",
        sticky="top",
        color="dark",
        dark=True,
    )

])

if __name__ == '__main__':
    app.run(host='192.168.25.68', port=8050, debug=True)

# pip install dash_daq
# pip install dash_bootstrap_components
# pip install pandas
# .venv\Scripts\activate