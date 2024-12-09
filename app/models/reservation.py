from app import db
from datetime import datetime, timezone

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    num_people = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='confirmed')
    


    notes = db.Column(db.String(500), nullable=True)
    reservation_type = db.Column(db.String(50), nullable=False, default="regular") # for integrations 3rd party
    is_confirmed = db.Column(db.Boolean(), nullable=False, default=False)
    is_cancelled = db.Column(db.Boolean(), nullable=False, default=False)
    cancelled_at = db.Column(db.DateTime, nullable=True)
    estimated_arrival = db.Column(db.DateTime, nullable=False)
    deposit_paid = db.Column(db.Boolean(), nullable=False, default=False)
    deposit_amount = db.Column(db.Float, nullable=True)
    reservation_status = db.Column(db.String(50), default='pending')

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))  
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=True)

    user = db.relationship('User', backref=db.backref('reservations', lazy=True))
    table_id = db.Column(db.Integer, db.ForeignKey('table.id'), nullable=True)
    table = db.relationship('Table', backref=db.backref('reservations', lazy=True))

    def __repr__(self):
        return f'<Reservation for {self.user.name} at {self.date}>'