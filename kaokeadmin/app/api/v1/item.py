from .. import api
from flask import jsonify, request
from flask_login import login_required
from ...models import Set, Item
from ... import db
import time

@api.route('/v1/item/<int:item_id>', methods=['GET'])
@login_required
def item(item_id):
	item = Item.query.get(item_id)
	data = {}
	if item is not None:
		data['id'] = item.id
		data['set_id'] = item.set_id
		data['title'] = item.title
		data['avatar'] = item.avatar
		data['origin_p'] = item.origin_p
		data['discount_p'] = item.discount_p
		data['content'] = item.content
		data['free'] = item.free
	return jsonify({'data':data,'errcode':0,'msg':'item detail'})

@api.route('/v1/item/add/<int:set_id>', methods=['POST'])
@login_required
def item_add(set_id):
	set = Set.query.get(set_id)
	if set is not None:
		title = request.json.get('title')
		avatar = request.json.get('avatar')
		content = request.json.get('content')
		free = request.json.get('free')
		product_n = long(time.time())
		item = Item(set_id=set_id,title=title,avatar=avatar,content=content,free=free,product_n=product_n)
		db.session.add(item)
		db.session.commit()
	return jsonify({'data':{},'errcode':0,'msg':'item add success'})

@api.route('/v1/item/mod/<int:item_id>', methods=['POST'])
@login_required
def item_modify(item_id):
	item = Item.query.get(item_id)
	if item is not None:
		item.title = request.json.get('title')
		item.avatar = request.json.get('avatar')
		item.content = request.json.get('content')
		item.free = request.json.get('free')
		db.session.add(item)
		db.session.commit()
	return jsonify({'data':{},'errcode':0,'msg':'modify item success'})

@api.route('/v1/item/del/<int:item_id>', methods=['POST'])
@login_required
def item_delete(item_id):
	item = Item.query.get(item_id)
	if item is not None:
		db.session.remove(item)
		db.session.commit()
	return jsonify({'data':{},'errcode':0,'msg':'delete item success'})