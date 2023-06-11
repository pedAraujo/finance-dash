# import stuff
# import os
# import json

# import firebase_admin
import logging

from flask import Flask
from .data.loader import load_transaction_data
from dotenv import load_dotenv


load_dotenv()

# logging configuration
logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("logs.log")],
)

# # Firebase initialization
# FIREBASE_ACCESS_JSON = json.loads(os.getenv("FIREBASE_CONFIG"))
# firebase_credentials = credentials.Certificate(FIREBASE_ACCESS_JSON)
# firebase_app = firebase_admin.initialize_app(firebase_credentials)

# Globally accessible variables
SPENDINGS_PATH = "data/despesas.csv"
REVENUE_PATH = "data/receita.csv"


# Create flask app
def init_app():
    app = Flask(__name__, static_folder="static", template_folder="templates")

    revenue_data = load_transaction_data(REVENUE_PATH)
    spendings_data = load_transaction_data(SPENDINGS_PATH)

    app.config.from_object("config")

    with app.app_context():
        # Include our Routes
        # from . import routes

        # Register Dashboard
        from .dash.dashboard import init_dashboard

        app = init_dashboard(app, revenue_data, spendings_data)

        return app
