from flask import Flask
from flask.ext.mongoengine import MongoEngine

app = Flask(__name__)

app.config.from_object('config')

db = MongoEngine(app)

def register_blueprints(app):
    from app.blog import blog
    from app.paser import paser
    app.register_blueprint(blog)
    app.register_blueprint(paser)

register_blueprints(app)

from app import models
