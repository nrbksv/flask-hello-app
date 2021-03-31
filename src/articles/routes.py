from flask import redirect, render_template, abort, request

from src import app, db
from src.articles.forms import ArticleForm
from src.articles.models import Article

from flask import Blueprint, url_for


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
    article = Article.query.get_or_404(article_id)
    return render_template('article_view.html', article=article)


@article_pages.route('/create/', methods=['GET', 'POST'])
def article_create():
    """
    Создание статьи
    """
    form = ArticleForm()
    if form.validate_on_submit():
        article = Article(
            title=form.title.data,
            content=form.content.data,
            author=form.author.data
        )
        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article_pages.article_list'))
    return render_template('create_article.html', form=form)


@article_pages.route('/<int:article_id>/update/', methods=['GET', 'POST'])
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

    if article_form.validate_on_submit():
        article.title = article_form.title.data
        article.content = article_form.content.data
        article.author = article_form.author.data

        db.session.add(article)
        db.session.commit()
        return redirect(url_for('article_pages.article_view', article_id=article_id))

    return render_template('update.html', form=article_form)


@article_pages.route('/<int:article_id>/delete/', methods=['GET', 'POST'])
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
