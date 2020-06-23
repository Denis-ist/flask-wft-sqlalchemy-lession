from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String())
    name = db.Column(db.String)
    age = db.Column(db.Integer)
    about = db.Column(db.String)

    def __repr__(self):
        return f'<User {self.email}>'


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)
    date_created = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Post text={self.text}>'

# db.create_all()
# db.session.commit()
