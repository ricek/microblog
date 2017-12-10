from flask import Flask
from pymongo import MongoClient
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
client = MongoClient(app.config['DATABASE_URI'])
db = client.test
login = LoginManager(app)
login.login_view = 'login'

# To avoid error from the mutal references
from app import routes
