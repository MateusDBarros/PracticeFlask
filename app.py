from flask import Flask, request, jsonify
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

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    field = db.Column(db.String(100), nullable=False)
    invest = db.Column(db.Float, nullable=False)
    
    def to_json(self):
        return {'id': self.id, 'name':self.name, 'field':self.field, 'invest':self.invest}

with app.app_context:
    db.create_all()
    
