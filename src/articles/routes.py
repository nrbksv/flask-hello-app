from flask import redirect, render_template, request
from flask_login import login_required

from src import db
from flask import Blueprint, url_for

from src.articles.models import Article, Comment
from src.articles.forms import ArticleForm, CommentForm

article_pages = Blueprint('article_pages', __name__, template_folder='templates')


@article_pages.route('/', methods=['GET'])
def article_list():
    """
    Список статей
    """
    articles = Article.query.all()
    return render_template('index.html', articles=articles)


@article_pages.route('/<int:article_id>/', methods=['GET'])
def article_view(article_id):
    """
    Детальная просмотр статьи
    """
    article_ = Article.query.get_or_404(article_id)
    comments = Comment.query.filter_by(article=article_.id).order_by(Comment.created_at.desc())
    form = CommentForm()
    return render_template('article_view.html', article=article_, comments=comments, form=form)


@article_pages.route('/create/', methods=['GET', 'POST'])
@login_required
def article_create():
    """
    Создание статьи
    """
    form = ArticleForm()
    if request.method == 'POST' and form.validate():
        form = ArticleForm(data=request.form)
        article = Article(
            author=form.author.data,
            title=form.title.data,
            content=form.content.data
        )
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article_pages.article_list'))
    return render_template('create_article.html', form=form)


@article_pages.route('/<int:article_id>/update/', methods=['GET', 'POST'])
@login_required
def article_update(article_id):
    """
    Редактирование статьи
    """
    article = Article.query.get_or_404(article_id)

    article_form = ArticleForm(
        title=article.title,
        content=article.content,
        author=article.author
    )

    if request.method == 'POST' and article_form.validate():
        article_form = ArticleForm(data=request.form)
        article.title = article_form.title.data
        article.content = article_form.content.data
        article.author = article_form.author.data

        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article_pages.article_view', article_id=article_id))

    return render_template('update.html', form=article_form)


@article_pages.route('/<int:article_id>/delete/', methods=['GET', 'POST'])
@login_required
def delete_article(article_id):
    """
    Удаление статьи
    """
    article = Article.query.get_or_404(article_id)

    if request.method == 'GET':
        return render_template('delete_article.html', article=article)

    db.session.delete(article)
    db.session.commit()
    return redirect(url_for('article_pages.article_list'))


@article_pages.route('/<int:article_id>/comment/add/', methods=['GET', 'POST'])
def add_comment(article_id):
    """
    Добавление комментария к статье
    """
    article = Article.query.get_or_404(article_id)
    form = CommentForm()
    if request.method == 'POST' and form.validate():
        form = CommentForm(data=request.form)
        comment = Comment(
            article=article_id,
            comment=form.comment.data,
            author=form.author.data
        )
        db.session.add(comment)
        db.session.commit()
        return redirect(url_for('article_pages.article_view', article_id=article_id))
    return render_template('article_view.html', article=article, form=form)
