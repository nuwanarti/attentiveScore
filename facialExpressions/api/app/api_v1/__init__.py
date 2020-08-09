from flask import Blueprint
from flask_restplus import Api
from flask_cors import CORS, cross_origin

api_v1 = Blueprint('api_v1', __name__)

api = Api(api_v1)
# cors = CORS(api)
# api.config['CORS_HEADERS'] = 'Content-Type'

from . import routes


