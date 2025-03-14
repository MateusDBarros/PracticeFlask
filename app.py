from flask import Flask
from sqlalchemy import SQLAlchemy
from urllib.parse import quote_plus

app = Flask(__name__)

USERNAME = 'postgres'
PASSWORD = quote_plus('lilY@')
HOST = 'localhost'
PORT = '5432'
DATABASE = 'practiceflask'

app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)