from flask import redirect, render_template, abort, request

from src import app
# from src.articles import article_pages
from src.articles.forms import ArticleForm

from flask import Blueprint


article_pages = Blueprint('article_pages', __name__, template_folder='templates')


articles = [  # Список, в котором хранятся наши статьи
    {'id': 1, 'title': 'Статья 1', 'content': 'Контент статьи 1', 'author': 'Vasya Pupkin'},
    {'id': 2, 'title': 'Статья 2', 'content': 'Контент статьи 2', 'author': 'Vasya Pupkin'},
    {'id': 3, 'title': 'Статья 3', 'content': 'Контент статьи 3', 'author': 'John Doe'},
    {'id': 4, 'title': 'Статья 4', 'content': 'Контент статьи 4', 'author': 'Vasya Pupkin'},
]


@article_pages.route('/', methods=['GET'])
def article_list():
    """
    Список статей
    """
    return render_template('index.html', articles=articles)


@article_pages.route('/<int:article_id>/', methods=['GET'])
def article_view(article_id):
    """
    Детальная просмотр статьи
    """
    article = get_article_or_404(article_id)
    return render_template('article_view.html', article=article)


@article_pages.route('/create/', methods=['GET', 'POST'])
def article_create():
    """
    Создание статьи
    """
    form = ArticleForm()
    if form.validate_on_submit():
        articles.append({
            'id': len(articles) + 1,
            'title': form.title.data,
            'content': form.content.data,
            'author': form.author.data
        })
        return redirect('/articles/')
    return render_template('create_article.html', form=form)


@article_pages.route('/<int:article_id>/update/', methods=['GET', 'POST'])
def article_update(article_id):
    """
    Редактирование статьи
    """
    article = get_article_or_404(article_id)

    article_form = ArticleForm(
        title=article.get('title'),
        content=article.get('content'),
        author=article.get('author')
    )

    if article_form.validate_on_submit():
        article['title'] = article_form.title.data
        article['content'] = article_form.content.data
        article['author'] = article_form.author.data
        return redirect(f'/articles/{article_id}/')

    return render_template('update.html', form=article_form)


def get_article_or_404(pk):
    for article in articles:
        if pk == article.get('id'):
            return article
    return abort(status=404)
