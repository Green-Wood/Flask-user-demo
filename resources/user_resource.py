from flask_restplus import Resource, Namespace, reqparse, fields
from models.user_model import UserModel
from resources.security import message_model


api = Namespace('user', description='User Operations')

# models
user_model = api.model('User', {
    'id': fields.Integer(description='User Identifier'),
    'username': fields.String(description='Username'),
})


@api.route('/<int:user_id>')
@api.doc(params={'user_id': '用户ID'})
@api.response(404, 'User not found', model=message_model)
class User(Resource):

    @api.marshal_with(user_model)
    def get(self, user_id):
        return UserModel.find_by_id(user_id)
