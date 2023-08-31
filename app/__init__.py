#  Copyright (c) 2023 Oackland Toro
#
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config
from .models import User, db
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    login_manager = LoginManager()
    db.init_app(app)
    migrate = Migrate(app, db)
    login_manager.init_app(app)

    login_manager.login_view = "login"
    login_manager.login_message = "danger"
    from .blueprints.auth import auth
    from .blueprints.main import main
    from .blueprints.pokemon import pokemon

    app.register_blueprint(pokemon)
    app.register_blueprint(main)
    app.register_blueprint(auth)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app
create_app()