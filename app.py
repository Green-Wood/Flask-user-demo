from flask import Flask
from flask_restplus import Api
from flask_jwt_extended import JWTManager
from db import db

from resources.user_resource import api as ns_user
from resources.security import api as ns_security

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost:5432/flask-user-demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['RESTPLUS_MASK_SWAGGER'] = False
app.secret_key = 'greenwood'

api = Api(app, version='1.0', title='User Demo Api')
db.init_app(app)
jwt = JWTManager(app)


api.add_namespace(ns_user)
api.add_namespace(ns_security)


@app.before_first_request
def create_tables():
    db.create_all()


if __name__ == '__main__':
    app.run(port=5000, debug=True)
