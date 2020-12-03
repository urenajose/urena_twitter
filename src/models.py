from flask_sqlalchemy import SQLAlchemy

DB = SQLAlchemy


class User(DB.model)gi
    id = DB.Column(DB.integer, primary_key=True)
    name = DB.Column(DB.string(30), nullable=False)


class Tweet(DB.model):
    id = DB.column(DB.integer, primary_key=True)
    text = DB.column(DB.Unicode(280), nullable=False)
    user_id = DB.Column(DB.Integer, DB.Foreignkey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets',lazy=True))

    def __repr__(self):
        return f'<Tweet: {self.text}>'
        