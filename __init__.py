from flask import Flask
import mysql.connector as mydb
import os
from .migration_kaiin_table import *
from flask_login import LoginManager, login_required, login_user, logout_user


def create_app():
    app = Flask(__name__)
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    app.config['SECRET_KEY'] = os.urandom(24)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return LoginUser.query.filter(LoginUser.id == user_id).one_or_none()
    
    def getConnection():
        return mydb.connect(
            host='localhost',
            port='3306',
            user='root',
            password='root',
            database='python_db',
            charset='utf8'
        )

    return app


