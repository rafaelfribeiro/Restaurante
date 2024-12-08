from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Reservation, Order

@app.route('/order/<int:reservation_id>', methods=['GET', 'POST'])
def order(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)

    if request.method == 'POST':
        item = request.form['item']
        quantity = request.form['quantity']

        new_order = Order(reservation_id=reservation_id, item=item, quantity=quantity)
        db.session.add(new_order)
        db.session.commit()

        return redirect(url_for('order', reservation_id=reservation_id))

    orders = Order.query.filter_by(reservation_id=reservation_id).all()
    return render_template('order.html', reservation=reservation, orders=orders)