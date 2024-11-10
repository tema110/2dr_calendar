from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    date = db.Column(db.String(10), nullable=False)
    time = db.Column(db.String(5), nullable=True)
    completed = db.Column(db.Boolean, default=False)