from .. import api
from ...models import Admin
from flask import jsonify, request
from flask_login import login_user, login_required, logout_user 

@api.route('/v1/auth/login', methods=['POST'])
def login():
	# request.args.get()
	# adminname = request.form['adminname']
	# password = request.form['password']
	adminname = request.json.get('account')
	password = request.json.get('password')
	if adminname is not None and password is not None:
		admin = Admin.query.filter_by(adminname=adminname).first()
		if admin is not None and admin.verify_password(password):
			login_user(admin, True)
			return jsonify({'data':{},'errcode':0,'msg':'login success'})
	return jsonify({'data':{},'errcode':10001,'msg':'fail'})

@api.route('/v1/auth/logout', methods=['POST'])
@login_required
def logout():
	logout_user()
	return jsonify({'data':{},'errcode':0,'msg':'logout success'})
