from app import db
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    item = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default='preparing')  # Status: preparing, ready, served

    reservation = db.relationship('Reservation', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        return f'<Order {self.item} - {self.status}>'