from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import Reservation

@app.route('/reservation', methods=['GET', 'POST'])
def reservation():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        date = request.form['date']
        time = request.form['time']
        num_people = request.form['num_people']

        new_reservation = Reservation(name=name, email=email, date=date, time=time, num_people=num_people)
        db.session.add(new_reservation)
        db.session.commit()

        return redirect(url_for('order', reservation_id=new_reservation.id))

    return render_template('reservation.html')