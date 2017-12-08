from flask import Flask

app = Flask(__name__)

# To avoid error from the mutal references
from app import routes
