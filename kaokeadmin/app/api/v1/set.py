from .. import api
from flask import jsonify, request
from flask_login import login_required
from ...models import Set, Item
from ... import db
import time

@api.route('/v1/set/home', methods=['GET'])
@login_required
def home():
	return jsonify({'data':{},'errcode':0,'msg':'home'})

@api.route('/v1/set/<int:set_id>', methods=['GET'])
@login_required
def set(set_id):
	set = Set.query.get(set_id)
	data = {}
	if set is not None:
		data['id'] = set.id
		data['title'] = set.title
		data['avatar'] = set.avatar
		data['origin_p'] = set.origin_p
		data['discount_p'] = set.discount_p
		data['desc'] = set.desc
		data['notice'] = set.notice
	return jsonify({'data':data,'errcode':0,'msg':'set detai'})

@api.route('/v1/set/all', methods=['GET'])
@login_required
def set_all():
	sets = Set.query.all()
	data = []
	for val in sets:
		set = {}
		set['id'] = val.id
		set['title'] = val.title
		set['avatar'] = val.avatar
		set['origin_p'] = val.origin_p
		set['discount_p'] = val.discount_p
		set['desc'] = val.desc
		set['notice'] = val.notice
		data.append(set)
		
	return jsonify({'data':data,'errcode':0,'msg':'get all sets success'})

@api.route('/v1/set/items/<int:set_id>', methods=['GET'])
@login_required
def set_items(set_id):
	set = Set.query.get(set_id)
	data = []
	if set is not None:
		for val in set.items:
			item = {}
			item['set_id'] = val.set_id
			item['id'] = val.id
			item['title'] = val.title
			item['avatar'] = set.avatar
			data.append(item)
	return jsonify({'data':data,'errcode':0,'msg':'set items'})

@api.route('/v1/set/add', methods=['POST'])
@login_required
def set_add():
	title = request.json.get('title')
	avatar = request.json.get('avatar')
	origin_p = request.json.get('origin_p')
	discount_p = request.json.get('discount_p')
	desc = request.json.get('desc')
	notice = request.json.get('notice')
	product_n = long(time.time())
	set = Set(title=title,avatar=avatar,desc=desc,notice=notice,origin_p=origin_p,discount_p=discount_p,product_n=product_n)
	db.session.add(set)
	db.session.commit()
	return jsonify({'data':{},'errcode':0,'msg':'add set success'})

@api.route('/v1/set/mod/<int:set_id>', methods=['POST'])
@login_required
def set_modify(set_id):
	set = Set.query.get(set_id)
	if set is not None:
		set.title = request.json.get('title')
		set.avatar = request.json.get('avatar')
		set.origin_p = request.json.get('origin_p')
		set.discount_p = request.json.get('discount_p')
		set.desc = request.json.get('desc')
		set.notice = request.json.get('notice')
		db.session.add(set)
		db.session.commit()
	return jsonify({'data':{},'errcode':0,'msg':'modify set success'})

@api.route('/v1/set/del/<int:set_id>', methods=['POST'])
@login_required
def set_delete(set_id):
	set = Set.query.get(set_id)
	if set is not None:
		db.session.remove(set)
		db.session.commit()
	return jsonify({'data':{},'errcode':0,'msg':'delete set success'})
