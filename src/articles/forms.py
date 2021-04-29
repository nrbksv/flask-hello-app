from wtforms_alchemy import ModelForm

from src.articles.models import Article, Comment


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'author']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'comment']
