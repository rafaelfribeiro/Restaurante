from app import db

class Table(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    table_number = db.Column(db.Integer, nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(50), default="available")

    reservations = db.relationship('Reservation', backref='table', lazy=True)

    def __repr__(self):
        return f'<Table {self.table_number}, Capacity {self.capacity}>'
    
# table1 = Table(table_number="A1", capacity=4, status="available")
# db.session.add(table1)
# db.session.commit()

# # Criando uma reserva associada a uma mesa
# reservation = Reservation(
#     user_id=1,
#     date=datetime.now(),
#     num_people=4,
#     table_id=table1.id  # Associando a reserva à mesa 1
# )
# db.session.add(reservation)
# db.session.commit()