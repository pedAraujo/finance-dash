import dash_bootstrap_components as dbc
from dash import html

TITLE = "Minhas Finanças"

logout_button = dbc.Button(
    children=[
        "Sair",
        html.I(className="navbutton-icon fa-solid fa-arrow-right-from-bracket"),
    ],
    className="navbar-logout-button",
    color="danger",
    n_clicks=0,
    # TODO: inserir href para logout
)

title = html.P(TITLE, className="navbar-title")


def render():
    return dbc.Navbar(
        children=[
            dbc.NavbarBrand(title),
            dbc.NavItem(logout_button),
        ],
        className="navbar",
    )
