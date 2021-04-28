from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import length, required


class ArticleForm(FlaskForm):
    title = StringField(label='Заголовок', validators=(required(), length(min=5, max=150)))
    content = TextAreaField(label='Контент', validators=(required(), length(min=20, max=1500)))
    author = StringField(label='Автор', validators=(required(), length(min=3, max=120)))


class CommentForm(FlaskForm):
    author = StringField(label='Автор', validators=(required(), length(max=150)))
    comment = TextAreaField(label='Комментарий', validators=(required(), length(max=2000)))
