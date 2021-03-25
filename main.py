from flask import (
    Flask,  # импортируем класс для инициализации flask-приложения
    render_template,  # импортируем функцию для рендера шаблонов (похожа на шоткат render в Django)
    abort,  # импортируем метод, который будет возвращать указанную ошибку
    redirect,  # импортируем функцию, которая будет делать редирект (похожа на шоткат redirect в Django)
    request,
    url_for
)

from forms import ArticleForm


articles = [  # Список, в котором хранятся наши статьи
    {'id': 1, 'title': 'Статья 1', 'content': 'Контент статьи 1', 'author': 'Vasya Pupkin'},
    {'id': 2, 'title': 'Статья 2', 'content': 'Контент статьи 2', 'author': 'Vasya Pupkin'},
    {'id': 3, 'title': 'Статья 3', 'content': 'Контент статьи 3', 'author': 'John Doe'},
    {'id': 4, 'title': 'Статья 4', 'content': 'Контент статьи 4', 'author': 'Vasya Pupkin'},
]


app = Flask(__name__)  # Инициализируем Flask-приложение
app.config['SECRET_KEY'] = 'secret_key'
app.config['ENV'] = 'development'


@app.route('/', methods=['GET'])
def index():
    """
    Представление для перенаправления пользователя с uri / на /articles/
    """
    return redirect(url_for('article_list'))


@app.route('/articles/', methods=['GET'])  # указываем нашему Flask-приложению, что это представление, которое будет обслуживать uri /articles/ и слушает только get-запросы
def article_list():
    """
    Представление для отображения списка статей
    """
    return render_template('index.html', articles=articles)  # Возвращаем ответ с отрендеренным шаблоном index.html. kwargs попадают в контекст шаблона


@app.route('/articles/<int:article_id>/', methods=['GET'])  # здесь в uri мы ожидаем получить целочисленный пареметр article_id
def article_view(article_id):  # параметр article_id попадает в kwargs, как и все параметры пути (uri)
    """
    Представление для отображения одной статьи
    """
    article = get_article(article_id)
    return render_template('article_view.html', article=article)  # отображаем шаблон article_view.htm, передавая в контекст шаблона статью


@app.route('/articles/create/', methods=['GET', 'POST'])
def article_create():
    form = ArticleForm()
    if form.validate_on_submit():
        articles.append({
            'id': len(articles) + 1,
            'title': form.title.data,
            'content': form.content.data,
            'author': form.author.data
        })
        return redirect(url_for('article_list'))

    return render_template('create_article.html', form=form)


@app.route('/articles/<int:article_id>/update/', methods=['GET', 'POST'])
def article_update(article_id):
    if request.method == 'GET':
        article = get_article(article_id)
        form = ArticleForm(
            title=article.get('title'),
            content=article.get('content'),
            author=article.get('author')
        )
        return render_template('update.html', form=form)
    elif request.method == 'POST':
        form = ArticleForm()
        if form.validate_on_submit():
            article = get_article(article_id)
            article['title'] = form.title.data
            article['content'] = form.content.data
            article['author'] = form.author.data
            return redirect(
                url_for('article_view', article_id=article_id))
        return render_template('update.html', form=form)


def get_article(pk):
    for article in articles:
        if pk == article.get('id'):
            return article
    return abort(status=404, description=('Файл не найден'))


if __name__ == '__main__':
    app.run(debug=True)  # запускаем наше Flask-приложение
