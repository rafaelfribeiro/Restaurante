from flask_user import UserMixin
from app import db
from datetime import datetime

class Role(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)

    def __repr__(self):
        return f'<Role {self.name}>'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(300), nullable=False)
    email = db.Column(db.String(200), nullable=True)
    password = db.Column(db.String(200), nullable=False)
    active = db.Column(db.Boolean(), nullable=False, default=True) 
    phone = db.Column(db.String(20), nullable=False, unique=True)

    created_at = db.Column(db.DateTime, default=datetime.now())  
    updated_at = db.Column(db.DateTime, default=None, onupdate=datetime.now(), nullable=True) 



    roles = db.relationship('Role', secondary='user_roles')

    def __repr__(self):
        return f'<User {self.name}>'


class UserRoles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))

    user = db.relationship(User, backref="user_roles")
    role = db.relationship(Role, backref="user_roles")