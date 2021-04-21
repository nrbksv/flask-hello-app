from datetime import datetime

from src import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    author = db.Column(db.String(150))
    comments = db.relationship('Comment', backref='comments')

    def __repr__(self):
        return f'<Article {self.id}: {self.title}>'


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text(2000))
    author = db.Column(db.String(150))
    article = db.Column(db.ForeignKey('article.id'))
    created_at = db.Column(db.DateTime(), default=datetime.utcnow)

    def __repr__(self):
        return f'{self.author}{self.comment}'