from flask import Flask
from extensions import db, csrf, bcrypt, migrate

app = Flask(__name__)
app.config.from_object("config")

db.init_app(app=app)
migrate.init_app(app=app, db=db)
csrf.init_app(app=app)
bcrypt.init_app(app=app)

from controlepagamentos import models


if __name__ == '__main__':
    app.run(debug=True)
