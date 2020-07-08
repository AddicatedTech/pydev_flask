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

app = Flask(__name__)
# 初始化 db 数据库对象  吧app和db绑定在一起，
# db = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/demo"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)
# 数据模型定义参数说明
# __tablename 表明
# id = db.Column("uid",db.Integer, primary_key=True)
# uid 影响的是该属性在表中的字段名 orm进行调用时则是使用id属性来调用


# 数据库操作
# 添加数据
@app.route("/")
def index():
	new_user = User(username="addicated", email="demo")
	db.session.add(new_user)
	db.session.commit()
	return "hello"


# 查询
@app.route("/")
def index():
	users = User.query.all()
	print(users)
	return "hello"


# -----------------------------------------------------


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# 延迟绑定也是可以的，下看另一种用法
# db.init_app(app)  # 初始化db绑定app，但是一定要在app路由生效之前（注意代码执行顺序）

class User(db.Model):
	__tablename__ = "user"
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True)
	email = db.Column(db.String(120), unique=True)


## 通过migrate 构建数据库
# 1，迁移的时候更加方便
# 2，可以动态修改db结构

migrate = Migrate(app, db)


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
