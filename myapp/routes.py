from flask import *
from flask_login import current_user, login_user, logout_user, login_required
from flask_mail import Message

from werkzeug.utils import secure_filename

from myapp import application, basedir, db
from myapp.forms import LoginForm, RegisterForm
from myapp.models import User



@application.route('/')
def splash():
    title = 'SpartanFitnessClub HomePage'
    return render_template("index.html", title=title)


@application.route('/register', methods=['GET', 'POST'])
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


@application.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    getuser = User.query.all()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        login_user(user)
        return redirect('/loggedin')
    return render_template("login.html", form=form)


@application.route('/loggedin')
@login_required
def log():
    flash('You are logged in', 'error')
    return redirect('/')


@application.route('/logout')
def logout():
    logout_user()
    flash('You are logged out', 'error')
    return redirect('/')


@application.route("/delete",)
def delete():
    user = User.query.filter_by(id=1).delete()
    db.session.commit()
    flash('Your account is deleted', 'error')
    return redirect("/register")