from src import db


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
    author = db.Column(db.String(150))

    def __repr__(self):
        return f'<Article {self.id}: {self.title}>'
