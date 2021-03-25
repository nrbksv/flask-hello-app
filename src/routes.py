from flask import redirect

from src import app


@app.route('/', methods=['GET'])
def index():
    return redirect('/articles/')
