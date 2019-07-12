from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request

'''
Create a flask app and configure the database
return: the app and the database
'''
def create_app():
    app = Flask(__name__)
    database_file = "sqlite:///games.db"
    app.config["SQLALCHEMY_DATABASE_URI"] = database_file

    db = SQLAlchemy(app)
    return db, app
