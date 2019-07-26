from flask_restplus import Resource, Namespace, reqparse, fields
import requests
from os import getenv

api = Namespace('model', description='ML model')

_cal_parser = reqparse.RequestParser()
_cal_parser.add_argument('instances', action='append', required=True, type=float)

predict_model = api.model(
    'predict',
    {
        'predict': fields.List(fields.Float)
    }
)


@api.route('/predict')
class Model(Resource):

    @api.response(200, 'predict successfully', model=predict_model)
    @api.expect(_cal_parser)
    def post(self):
        data = _cal_parser.parse_args()
        MODEL_HOST = getenv('MODEL_HOST', 'localhost')
        MODEL_URI = '{host}:8501/v1/models/half_plus_two:predict'.format(host=MODEL_HOST)
        session = requests.Session()
        session.trust_env = False
        response = requests.post(MODEL_URI, json=data)
        if not response.ok:
            return 'something goes wrong', 400
        return MODEL_URI, 200
