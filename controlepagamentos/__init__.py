from flask import Flask
from extensions import db, csrf, bcrypt, migrate, login_manager
from controlepagamentos import models
from controlepagamentos.views import bp


def create_app():
    app = Flask(__name__)
    app.config.from_object("config")

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    csrf.init_app(app=app)
    bcrypt.init_app(app=app)
    login_manager.init_app(app=app)

    login_manager.login_view = 'login'   # Redireciona para a página lgoin que é a função definida no routes.py
    login_manager.login_message = "Você precisa estar logado para acessar esta página."
    login_manager.login_message_category = 'alert-info'

    app.register_blueprint(bp)
    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
