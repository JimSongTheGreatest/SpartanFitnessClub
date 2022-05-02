from flask import *
from flask_login import current_user, login_user, logout_user, login_required
# from flask_mail import Message

from werkzeug.utils import secure_filename

from sfc import db
from sfc.forms import LoginForm, RegisterForm
from sfc.models import User

bp = Blueprint('routes', __name__, url_prefix='/')


@bp.route('/')
def splash():
    title = 'Spartan Fitness Club'
    return render_template("index.html", title=title)


@bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
   # all_users = User.query.all()

    if form.validate_on_submit():
        new_user = User(username=form.username.data,
                        password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You are registered', 'error')
        return redirect("/login")
    return render_template("register.html", form=form)


@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    getuser = User.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect('/loggedin')
    return render_template("login.html", form=form)


@bp.route('/loggedin')
@login_required
def log():
    flash('You are logged in', 'error')
    return redirect('/')


@bp.route('/logout')
def logout():
    logout_user()
    flash('You are logged out', 'error')
    return redirect('/')


@bp.route("/delete",)
def delete():
    user = User.query.filter_by(id=1).delete()
    db.session.commit()
    flash('Your account is deleted', 'error')
    return redirect("/register")
