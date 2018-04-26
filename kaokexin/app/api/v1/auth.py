from .. import api
from flask import jsonify

@api.route('/v1/auth/login')
def login():
	return jsonify({'data':{},'code':0,'msg':'ok'})