from . import db

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column('id', db.Integer, primary_key=True)
    username = db.Column('username', db.String(50), nullable=False, unique=True)
    gender = db.Column('gender', db.String(1), nullable=False)
    email = db.Column('email', db.String(50), nullable=False)
    password_hashed = db.Column('password_hashed', db.String(200), nullable=False)
    
    def __init__(self, username, gender, email, password_hashed):
        self.username = username
        self.gender = gender
        self.email = email
        self.password_hashed = password_hashed
        
    def __repr__(self):
        return f'<User {self.username}>'