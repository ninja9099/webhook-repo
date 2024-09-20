from flask import Flask

from app.main.routes import main
from app.webhook.routes import webhook


# Creating our flask app
def create_app():

    app = Flask(__name__)

    # registering all the blueprints
    app.register_blueprint(main)
    app.register_blueprint(webhook)

    return app
