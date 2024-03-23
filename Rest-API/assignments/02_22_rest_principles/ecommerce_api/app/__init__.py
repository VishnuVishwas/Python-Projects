# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_jwt_extended import JWTManager

# flask app instance
app = Flask(__name__)
app.config['SECRET_KEY'] = '7ed9fc6681b07238e4fc077152e171d4'

# setting up db config and instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

api = Api(app)
jwt = JWTManager(app)

