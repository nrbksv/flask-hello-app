from flask import request, render_template, Blueprint, redirect, url_for, abort
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash

from src.auth.forms import LoginForm
from src.auth.models import User

auth_pages = Blueprint('auth_pages', __name__, template_folder='templates')


@auth_pages.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)

    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('article_pages.article_list'))
        abort(400)
    return render_template('login.html', form=form)


@login_required
@auth_pages.route("/logout/")
def logout():
    logout_user()
    return redirect(url_for('auth_pages.login'))
