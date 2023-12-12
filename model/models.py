from model import db

# DB model to save the results in the MySQL DB
class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64))
    result = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, text, result, user_id):
        self.text = text
        self.result = result
        self.user_id = user_id

# DB model to save the users in the MySQL DB
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
    results = db.relationship('Results', backref='user', lazy=True)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
