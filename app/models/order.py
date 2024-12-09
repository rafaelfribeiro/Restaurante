from app import db
from datetime import datetime, timezone
from sqlalchemy import Enum

class StatusEnum(Enum):
    PENDING = "pending"
    IN_PREPARATION = "in preparation"
    READY = "ready"
    DELIVERED = "delivered"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, index=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=True, index=True)
    status = db.Column(Enum(StatusEnum), default=StatusEnum.PENDING)
    total_amount = db.Column(db.Float, nullable=False, default=0.0)

    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))
    updated_at = db.Column(db.DateTime, default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc), nullable=True)

    items = db.relationship('OrderItem', backref='order', lazy=True)

    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    reservation = db.relationship('Reservation', backref=db.backref('orders', lazy=True))

    def __repr__(self):
        item_names = ', '.join([item.item_name for item in self.items])
        return f'<Order #{self.id} for {self.user.name} with items: {item_names} and total of ${self.total_amount} and status {self.status}>'

    def calculate_total(self):
        self.total_amount = sum(item.total for item in self.items)
        db.session.commit()

class OrderItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), nullable=False)
    item_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def calculate_total(self):
        self.total = self.quantity * self.price
        db.session.commit()
        self.order.calculate_total()

    

    def __repr__(self):
        return f'<OrderItem {self.item_name}: \nQuantity {self.quantity} \nPrice {self.price} \nTotal {self.total}>'    
    




# # Criar um pedido
# order = Order(user_id=1, status="pending", total_amount=0.0)
# db.session.add(order)
# db.session.commit()

# # Adicionar itens ao pedido
# item1 = OrderItem(order_id=order.id, item_name="Pizza", quantity=2, price=15.0, total=30.0)
# item2 = OrderItem(order_id=order.id, item_name="Coca-Cola", quantity=1, price=5.0, total=5.0)

# # Adicionar os itens ao pedido
# db.session.add(item1)
# db.session.add(item2)
# db.session.commit()

# # Atualizar o valor total do pedido
# order.update_total_amount()
