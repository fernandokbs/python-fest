from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
