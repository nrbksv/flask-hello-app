from flask_login import UserMixin

from src import db, login_manager
from werkzeug.security import generate_password_hash


@login_manager.user_loader
def load_user(user_id):
    user_id = int(user_id)
    return User.query.get(user_id)


class User(UserMixin, db.Model):
    __table_args__ = (
        db.UniqueConstraint('login', name='unique_login_cnstr'),
    )
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(150))
    password = db.Column(db.String(150))

    def __repr__(self):
        return self.login

    def set_password(self, password: str):
        self.password = generate_password_hash(password)
