from flask import (
    Flask,  # импортируем класс для инициализации flask-приложения
    render_template,  # импортируем функцию для рендера шаблонов (похожа на шоткат render в Django)
    abort,  # импортируем метод, который будет возвращать указанную ошибку
    redirect,  # импортируем функцию, которая будет делать редирект (похожа на шоткат redirect в Django)
    request
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


@app.route('/', methods=['GET'])
def index():
    """
    Представление для перенаправления пользователя с uri / на /articles/
    """
    return redirect('/articles/')


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
    for article in articles:  # перебираем все статьи
        if article_id == article['id']:  # если id перебираемой статьи соответствет значению параметра article_id
            return render_template('article_view.html', article=article)  # отображаем шаблон article_view.htm, передавая в контекст шаблона статью
    return abort(404)  # после того, как все статьи были перебраны и статья с нужны id не нашлась - возвращаем ошибку с 404 статус-кодом


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
        return redirect('/articles/')
    return render_template('create_article.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)  # запускаем наше Flask-приложение
