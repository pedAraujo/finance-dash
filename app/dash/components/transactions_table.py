from dash import dash_table, html
from . import ids
from ...data.loader import DataSchema


def render(app, revenue_data, spendings_data) -> html.Div:
    df = revenue_data

    return html.Div(
        [
            dash_table.DataTable(
                df.to_dict("records"),
                [{"name": i, "id": i} for i in df.columns],
            ),
        ],
    )
