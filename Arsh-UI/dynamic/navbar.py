import dash_bootstrap_components as dbc

def create_navbar():
    # Create the Navbar using Dash Bootstrap Components
    navbar = dbc.NavbarSimple(
        children=[
            dbc.DropdownMenu(
                nav=True,
                in_navbar=True,
                label="Menu",  # Label given to the dropdown menu
                children=[
                    # In this part of the code we create the items that will appear in the dropdown menu on the right
                    # side of the Navbar.  The first parameter is the text that appears and the second parameter
                    # is the URL extension.
                    dbc.DropdownMenuItem("Home", href='/'),  # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem(divider=True),  # Divider item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Page 2", href='/page-2'),  # Hyperlink item that appears in the dropdown menu
                    dbc.DropdownMenuItem("Page 3", href='/page-3'),  # Hyperlink item that appears in the dropdown menu
                ],
            ),
        ],
        brand="Smart Home",
        brand_href="/",
        sticky="top",
        color="dark",
        dark=True,
    )

    return navbar
