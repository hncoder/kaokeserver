from .. import api
from ... import login_manager
from flask import jsonify

ErrCodeUnauthorized = 10001

@login_manager.unauthorized_handler
def unauthorized_handler():
	return error_unauthorized()

def error_unauthorized():
	response = jsonify({'msg':'unauthorized','data':{},'errcode':ErrCodeUnauthorized})
	response.status_code = 200
	return response