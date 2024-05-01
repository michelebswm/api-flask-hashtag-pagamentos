from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
migrate = Migrate()
csrf = CSRFProtect()
bcrypt = Bcrypt()
