from app import db


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), unique=True)


    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<Model {}>'.format(self.name)



