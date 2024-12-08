from app import db
from datetime import datetime
class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    num_people = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='confirmed')  # Status: confirmed, cancelled

    user = db.relationship('User', backref=db.backref('reservations', lazy=True))

    def __repr__(self):
        return f'<Reservation {self.date}>'