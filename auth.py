from flask import Blueprint, Flask, flash, render_template, request, redirect, url_for
from .migration_kaiin_table import *
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET'])
def form():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')
    #user = session.query(User).filter(User.email==email).first()
    user = LoginUser.query.filter(LoginUser.email == email).one_or_none()
    if user == None:
        flash("指定のユーザーは存在しません", "failed")
        return render_template('login.html')

    print("pass:[" + password + "]")
    print("db pass:[" + user.password + "]")

    if not check_password_hash(user.password, password):
        flash("パスワードが違います", "failed")
        return render_template('login.html')

    login_user(user)
    return redirect(url_for('main.profile'))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/signup', methods=['GET'])
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    user = User(name=name, email=email, password=generate_password_hash(password, method='sha256'))
    session.add(user)
    session.commit()
    return redirect(url_for('auth.login'))
