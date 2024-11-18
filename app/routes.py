from flask import Blueprint, render_template, request, redirect, url_for, flash
from sqlalchemy import text
from . import db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/users')
def list_users():
    query = "SELECT * FROM Users"
    result = db.session.execute(text(query))
    users = result.fetchall()
    return render_template('table.html', rows=users, table_name="Users")

@main.route('/users/add', methods=['GET', 'POST'])
def add_user():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        surname = request.form.get('surname')
        salary = request.form.get('salary')
        phone = request.form.get('phone')
        cname = request.form.get('cname')

        query = """
        INSERT INTO Users (email, name, surname, salary, phone, cname)
        VALUES (:email, :name, :surname, :salary, :phone, :cname)
        """
        db.session.execute(
            text(query),
            {'email': email, 'name': name, 'surname': surname, 'salary': salary, 'phone': phone, 'cname': cname}
        )
        db.session.commit()
        flash("User added successfully!")
        return redirect(url_for('main.list_users'))
    return render_template('form.html', table_name="Users")

# Add similar CRUD routes for other tables like Patients, Disease, etc.
