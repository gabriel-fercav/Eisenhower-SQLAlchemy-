import os
from flask import Flask
from dotenv import load_dotenv
from app.configs import database, migrations
from app import routes

load_dotenv()

def create_app():    
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_SORT_KEYS'] = False
    
    database.init_app(app)
    migrations.init_app(app)
    
    routes.init_app(app)
    
    return app
