from flask_script import Commnad
from flask_blog import app, db

class InitDB(Commnad):
    "create database"

    def run(self):
        with app.app_context():
            db.create_all()
