#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 18:50
# @Author  : Addicated
# @Site    : 
# @File    : app1.py
# @Software: PyCharm
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask
from sqlalchemy.orm import Query
from sqlalchemy.sql.operators import ColumnOperators

app = Flask(__name__)
# 初始化 db 数据库对象  吧app和db绑定在一起，
# db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/demo"
# mysql+pymysql://root:@localhost:3306/demo
# 数据库类型，数据操作模块,使用sqlite(3个斜杠，linux下4个斜杠
# 当一个项目需要使用多个db的时候 使用sqlalchemy_binds的配置字段进行设置
# --------- 一个项目使用多个数据库的情况下 ，绑定多个db
# app.config['SQLALCHEMY_BINDS']={
# 	'users':"sqlite:///d:/demo1.db"
# }
#

# 模型类也要绑定
# class user(db.Model):
#       __bind_key__ ="user"

# ----------------------------------------


# -------------------------- 数据模型定义的参数说明
# class User(db.Model):
# 	__tablename__="user"
# 	id = db.Column(db.Integer,primary_key=True)
# 	username  = db.Column(db.String(80),unique=True)
# 	email  = db.Column(db.String(120),unique=True)

# db.Model 继承db下面的基类，与db进行绑定
# db.Column
# 最常的数据格式
# db.String 字符串需要指明长度
# db.Text 长的unicode文本
# DateTime  表示为python datetime 对象的时间和日企
# intger
# smallintger
# float
# Boolean 存储布尔值
# PickleType 存储为一个持久化的python对象
# LargeBinary 存储一个任意大的二进制数据


 # 参数
 # db.ForeginKey('project.id')
 # primary.key  主键，唯一标示
 # autoincrement 自增长
 # unique  唯一
 # index  索引可以极大的提高查询的速度，但是索引很多的话，查询速度会降低，且写入速度会降低
 # nullable  不为空
 # default   默认
 # comment  说明，注释
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db = SQLAlchemy(app)
class User(db.Model):
	__tablename__="user"
	id = db.Column(db.Integer,primary_key=True)
	username  = db.Column(db.String(80),unique=True)
	email  = db.Column(db.String(120),unique=True)
# 数据库操作
# 添加数据
@app.route("/")
def index():
	new_user = User(username="addicated",email="demo")
	db.session.add(new_user)
	db.session.commit()
	return "hello"
# 查询
@app.route("/")
def index():
	users = User.query.all()
	print(users)
	return "hello"
#################################
# 7.9 插入行
user =User(username="demo")
db.session.add(user)
# 添加多个
# db.session.add_all([user1,user2])

# 事务，一连串的数据库操作、
# 加一个异常处理，如果报错了就rollback
try:
	db.session.commit()  # 只有在commit的时候才会生效到数据库中
except:
	db.session.rollback()
# query  sqlalchemy 下的
# 查询和过滤
# 可以通过官方文档或者query原码查看相关函数
# orm
# 1，所有的all()  查询满足条件的所有字段
# users= User.query.where().group_by().offset().all() # 支持链式调用
users = User.query.all()
# 基本原理是每个方法都返回一个统一的方法，之后就可以一直调用下去
# 直到返回的不再是同一个对象或者方法

# 2,first  拿到查询的第一个结果
user = User.query.first()

# 3，get方法 要通过主键去获取 主键唯一，是一个位置参数
user = User.query.get(5)  # 位置传参，不能
# 表内有多个主键的情况下，使用元祖传入进去
# 或者使用字典 kv方式传入进去
# 如果没获取到，会返回一个None，获取到的话会返回一个模型
# 如果没返回数据，想要其报错的话，
Query.get_or_404()


# 4,filter_by()
#   第一种 使用filter_by方法
Query.filter_by()

# 5 filter() 进行更为复杂的查询
Query.filter()  # 位置传参
User.query.filter(User.email.endswith("xxx")).all()
# 支持字段很多，在ColumnOperators中进行确认
ColumnOperators
# -----------------------------------------------------



app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False
db = SQLAlchemy(app)
# 延迟绑定也是可以的，下看另一种用法
# db.init_app(app)  # 初始化db绑定app，但是一定要在app路由生效之前（注意代码执行顺序）

class User(db.Model):
	__tablename__="user"
	id = db.Column(db.Integer,primary_key=True)
	username  = db.Column(db.String(80),unique=True)
	email  = db.Column(db.String(120),unique=True)
## 通过migrate 构建数据库
# 1，迁移的时候更加方便
# 2，可以动态修改db结构

migrate = Migrate(app,db)
# migrate 方式的常用命令
# 初始化 falsk db init
# 这个命令将会新建一个名字为migrations的文件夹，并记录一个数据库版本号
# 一份保留在migrations中，一份保存在数据库中(新建一张名字为alembic_version的表来保存)，
# 值得注意大是新建了migrations文件夹后需要对数据库模型进行修改，然后使用flask-migrations进行迁移，
# 这样才产生第一个版本号。

# 数据迁移
# flask db migrate
# 迁移脚本最好仔细审查按需编写

# 升级
# flask db upgrade
# 每次db模型变化，需要重复使用migrate命令和upgrade命令，按照顺序组合使用，成功后修改版本号

# 帮助
# flask db --help 查看更多命令的帮助信息

@app.route('/')
def index():
	return "hello"
# current_app  # 代理的request这么一个类  在请求过程中，
# 只要是访问路由，就可以通过current_app来获取到其他东西
# 比如current_app.config
# app同样可以获取到，为什么使用current_app.config?

# 是为了线程安全，通常一个app路由内只有一个请求，
# current_app里面的属性是不会跑的别的app请求中去的
# 在其他文件中想访问app的资源就需要使用current_app来进行访问

# 主要使用场景，大型项目里面，app.py文件是分包的
'''
current_app = LocalProxy(_find_app)
request = LocalProxy(partial(_lookup_req_object, "request"))
session = LocalProxy(partial(_lookup_req_object, "session"))
g = LocalProxy(partial(_lookup_app_object, "g"))
'''
if __name__ == '__main__':
	app.run(debug=True)
