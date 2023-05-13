# import stuff
from flask import Flask
from .data.loader import load_transaction_data

# from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
# database = SQLAlchemy()
SPENDINGS_PATH = "data/despesas.csv"
REVENUE_PATH = "data/receita.csv"


# Create flask app
def init_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    revenue_data = load_transaction_data(REVENUE_PATH)
    spendings_data = load_transaction_data(SPENDINGS_PATH)

    # derive configuration values
    app.config.from_object("config")

    # Initialize Plugins (the global ones)
    # database.init_app(app)

    # define context
    with app.app_context():
        # Include our Routes
        # from . import routes
        from .dash.dashboard import init_dashboard

        app = init_dashboard(app, revenue_data, spendings_data)

        # Register Blueprints
        return app
