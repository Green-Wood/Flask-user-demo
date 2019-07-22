from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from db import db
from config import config
from os import getenv

from resources.user_resource import api as ns_user
from resources.security import api as ns_security

# choose a env {'dev', 'test', 'prod'}
APP_ENV = getenv('APP_ENV', 'dev')
app = Flask(__name__)
app.config.from_object(config[APP_ENV])

api = Api(app, version='1.0', title='User Demo Api', prefix='/api')
db.init_app(app)
jwt = JWTManager(app)


api.add_namespace(ns_user)
api.add_namespace(ns_security)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
