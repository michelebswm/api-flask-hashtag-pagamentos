from flask import Flask
from extensions import db, csrf, bcrypt, migrate, login_manager

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

from controlepagamentos import views


if __name__ == '__main__':
    app.run(debug=True)
