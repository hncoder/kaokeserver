#encoding:utf-8 
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from datetime import datetime

class Role(db.Model):
	"""docstring for Role"""
	__tablename__ = 'kk_roles'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	name = db.Column(db.String(64), unique=True)
	admins = db.relationship('Admin', backref='role', lazy='dynamic')

	def __repr__(self):
		return '<Role %r>' % self.name


class Admin(UserMixin,db.Model):
	"""docstring for Admin"""
	__tablename__ = 'kk_admins'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	email = db.Column(db.String(64), unique=True, index=True)
	adminname = db.Column(db.String(64), unique=True, index=True)
	sex = db.Column(db.SMALLINT, default=0)
	role_id = db.Column(db.Integer, db.ForeignKey('kk_roles.id'))
	password_hash = db.Column(db.String(128))
	confirmed = db.Column(db.Boolean, default=False)
	@property
	def password(self):
		raise AttributeError('password is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)

	def __repr__(self):
		return '<Admin %r>' % self.adminname

@login_manager.user_loader
def load_user(id):
    return Admin.query.get(int(id))

class User(db.Model):
	"""docstring for User"""
	__tablename__ = 'kk_users'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	union_id = db.Column(db.String(100), unique=True, index=True)# comment='联合id'
	open_id = db.Column(db.String(100))# comment='开放id'
	platform = db.Column(db.SMALLINT, default=0) # comment='来自平台'
	nickname = db.Column(db.String(100)) # comment='用户昵称'
	avatar = db.Column(db.String(500)) # comment='用户头像'
	sex = db.Column(db.SMALLINT, default=0) # comment='用户性别'
	phone = db.Column(db.String(20)) # comment='用户电话'
	province = db.Column(db.String(20)) # comment='用户省份'
	city = db.Column(db.String(20)) # comment='用户城市'
	register_t = db.Column(db.DateTime, default=datetime.now) # comment='时间戳'
	orders = db.relationship('Order', backref='user', lazy='dynamic')

	def __repr__(self):
		return '<User %r>' % self.nickname

class Set(db.Model):
	"""docstring for Set"""
	__tablename__ = 'kk_sets'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	product_n = db.Column(db.Integer, unique=True, index=True) # comment='商品号'
	type = db.Column(db.SMALLINT, default=0) # comment='课程类型'
	title = db.Column(db.String(200)) # comment='课程标题'
	avatar = db.Column(db.String(500)) # comment='课程封面'
	desc = db.Column(db.Text) # comment='课程描述'
	notice = db.Column(db.Text) # comment='课程须知'
	create_t = db.Column(db.DateTime, default=datetime.now) # comment='创建时间'
	modify_t = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # comment='修改时间'
	origin_p = db.Column(db.Integer, default=0) # comment='原价'
	discount_p = db.Column(db.Integer, default=0) # comment='折扣价'
	items = db.relationship('Item', backref='set', lazy='dynamic')
	orders = db.relationship('Order', backref='set', lazy='dynamic')

	def __repr__(self):
		return '<Set %r>' % self.title

class Item(db.Model):
	"""docstring for Item"""
	__tablename__ = 'kk_items'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	product_n = db.Column(db.Integer, unique=True, index=True) # comment='商品号'
	set_id = db.Column(db.Integer, db.ForeignKey('kk_sets.id')) # comment='课程id'
	index = db.Column(db.Integer) # comment='课程内序列号'
	type = db.Column(db.SMALLINT, default=0) # comment='内容类型'
	title = db.Column(db.String(200)) # comment='内容标题'
	avatar = db.Column(db.String(500)) # comment='内容封面'
	content = db.Column(db.Text) # comment='内容封面'
	create_t = db.Column(db.DateTime, default=datetime.now) # comment='创建时间'
	modify_t = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now) # comment='修改时间'
	free = db.Column(db.Boolean, default=False) #comment='免费'
	origin_p = db.Column(db.Integer, default=0) # comment='原价'
	discount_p = db.Column(db.Integer, default=0) # comment='折扣价'
	orders = db.relationship('Order', backref='item', lazy='dynamic')

	def __repr__(self):
		return '<Set %r>' % self.title

class Order(db.Model):
	"""docstring for Order"""
	__tablename__ = 'kk_orders'
	id = db.Column(db.Integer, primary_key=True, autoincrement=True)
	set_n = db.Column(db.Integer, db.ForeignKey('kk_sets.product_n')) # comment='商品号'
	item_n = db.Column(db.Integer, db.ForeignKey('kk_items.product_n')) # comment='商品号'
	user_id = db.Column(db.Integer, db.ForeignKey('kk_users.id')) # comment='用户ID'
	pay_n = db.Column(db.String(100), unique=True, index=True) # comment='支付流水号'
	create_t = db.Column(db.DateTime, default=datetime.now) # comment='订单创建时间'
	pay_t = db.Column(db.DateTime) # comment='订单支付时间'
	status = db.Column(db.SMALLINT) # comment='订单状态'

	def __repr__(self):
		return '<Order %r>' % self.pay_n

		

		
		
