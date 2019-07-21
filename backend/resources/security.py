from flask_restplus import Resource, Namespace, reqparse, fields
from backend.models.user_model import UserModel
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token
)

api = Namespace('security', description='Security')

# reqparse
_user_parser = reqparse.RequestParser()
_user_parser.add_argument('username',
                          type=str,
                          required=True,
                          help="用户名",
                          )
_user_parser.add_argument('password',
                          type=str,
                          required=True,
                          help="密码",
                          )

message_model = api.model(
    'message_model',
    {'message': fields.String}
)

user_login_model = api.model(
    'user_login_model',
    {
        'access_token': fields.String,
        'refresh_token': fields.String,
        'user_id': fields.Integer
    }
)


@api.route('/register')
class UserRegister(Resource):

    @api.expect(_user_parser)
    @api.response(201, 'User created successfully', model=message_model)
    @api.response(400, 'Username already used', model=message_model)
    def post(self):
        '''Register a user'''
        data = _user_parser.parse_args()
        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(**data)
        user.save()

        return {"message": "User created successfully."}, 201


@api.route('/login')
class UserLogin(Resource):

    @api.expect(_user_parser)
    @api.response(200, 'Login successfully', model=user_login_model)
    @api.response(401, 'Unauthorized user', model=message_model)
    def post(self):
        '''Login System, return Token'''
        data = _user_parser.parse_args()
        user = UserModel.find_by_username(data['username'])

        if user and user.password == data['password']:
            access_token = create_access_token(identity=user.id, fresh=True)
            refresh_token = create_refresh_token(user.id)
            return {
                       'access_token': access_token,
                       'refresh_token': refresh_token,
                       'user_id': user.id
                   }, 200

        return {'message': 'Invalid username or password'}, 401
