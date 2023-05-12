# import stuff
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
database = SQLAlchemy()


# Create flask app
def init_app():
    app = Flask(__name__, instance_relative_config=False)

    # derive configuration values
    app.config.from_object("config.Config")

    # Initialize Plugins (the global ones)
    database.init_app(app)

    # define context
    with app.app_context():
        # Include our Routes
        from . import routes

        # Register Blueprints
        return app
