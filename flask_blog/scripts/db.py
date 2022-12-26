from flask_script import Command
from flask_blog import app, db

class InitDB(Command):
    "create database"

    def run(self):
        db.create_all()

#with app.app_context():
#   db.create_all()