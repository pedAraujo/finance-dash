from dash import html
from .navbar import navbar

# from . import ids
from . import year_dropdown, month_dropdown


def create_layout(dash_app, revenue_data, spendings_data) -> html.Div:
    # creates layout object for dashboard

    dash_app.layout = html.Div(
        children=[
            navbar(),
            html.Div(
                className="dropdown-container",
                children=[
                    year_dropdown.render(dash_app, revenue_data, spendings_data),
                    month_dropdown.render(dash_app, revenue_data, spendings_data),
                ],
            ),
        ]
    )

    return dash_app.layout
