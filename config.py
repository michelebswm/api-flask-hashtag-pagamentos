import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
SECRET_KEY = os.environ.get("SECRET_KEY")
TOKEN_CREATE = os.environ.get("TOKEN_CREATE")
FLASK_RUN_PORT = os.environ.get("FLASK_RUN_PORT", 8000)
