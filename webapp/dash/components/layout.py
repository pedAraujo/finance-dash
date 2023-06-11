from dash import html
import dash_bootstrap_components as dbc

from . import navbar
from . import year_dropdown
from . import month_dropdown
from . import day_dropdown
from . import transactions_table


def create_layout(dash_app, revenue_data, spendings_data) -> html.Div:
    # creates layout object for dashboard

    dash_app.layout = dbc.Container(
        [
            navbar.render(),
            dbc.Row(
                [transactions_table.render(dash_app, revenue_data, spendings_data)]
            ),
        ],
        fluid=True,
        class_name="dash-body-container",
    )
    return dash_app.layout
