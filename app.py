from application.database import db
from flask import Flask
from application.config import LocalDevelopmentConfig
import os

app = None

def create_app_instance():
    app = Flask(__name__, template_folder="templates")
    app.config.from_object(LocalDevelopmentConfig)
    db.init_app(app)
    app.app_context().push()
    # db.create_all()
    return app

app = create_app_instance()

from application.controllers import *


if __name__ == "__main__":
    app.run(host="0.0.0.0")
