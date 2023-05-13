import dash_bootstrap_components as dbc

TITLE = "Minhas Finanças"


def navbar():
    return dbc.Navbar(
        className="navbar",
        children=[
            dbc.NavbarBrand(TITLE),
            dbc.Button(
                "Sair", color="danger", id="logout-button", size="sm", n_clicks=0
            ),
        ],
    )
