import os

import pymysql
from flask import Flask, request, render_template, g
from helpers.forms import RegisterForm

app = Flask(__name__)

from flask_wtf import FlaskForm
from flask_wtf import Form

app.config["SECRET_KEY"] = os.urandom(24)  # 秘钥设置任意


@app.route('/')
def hello_world():
	# 验证
	return 'Hello World!'


# 在某个请求之前，就会在任何一个请求之前进行被装饰的钩子方法
@app.before_request
def get_num_of_interface():
	print("访问计数+1")


@app.after_request
def after(response):
	print("after", request.url)
	response.headers['you'] = 'love'
	return response


# response参数必须传，return必须是一个response对象
# 通常用来修改响应
# 如果访问的视图出现错误，则不会调用

# ---------g变量实例
def connect_to_database():
	conn = pymysql.connect()
	return conn.cursor()


@app.before_request
def get_db():
	if 'db' not in g:
		# 检测如果不在就进行连接DB
		g.db = connect_to_database()


@app.teardown_request
def teardown_db(exception):
	# pop方法移除db变量
	db = g.pop('db', None)
	if db is not None:
		db.close();
# -----end ----g变量实例


# 视图中进行使用
@app.route("/register")
def reg():
	g.db.execute("sql")
	a = g.db.fetchall()
	print(a)


# 使用表单验证器
# 引入
@app.route('/register', methods=['GET', 'POST'], endpoint="register")
def register():
	form = RegisterForm(request.form)
	# 	form = RegisterForm(request.form)
	# 如果传送请求信息不是通过form表单传过来的，会默认去检索obj
	# obj 可以是一个类
	# 传输数据的优先级以及判断
	#     def __init__(self,
	#     formdata=None, obj=None, prefix='', data=None, meta=None, **kwargs):
	# 先判断是否有 formdata ，即request中的form对象，
	# 之后 obj 主要应用与不同请求方式，比如ajax，再接收数据的时候就要进行配置
	# 在之后 data ，data需要是一个字典格式，比如json数据

	# 调用的时候，从表单模块拿到验证类，然后将前端提交的form信息传入
	# 然后调用生成form对象的validate方法进行验证，返回值为布尔型
	# true 成功，false 失败
	if request.method == "GET":
		return render_template("register.html", form=form)
	# get请求的时候将form对象传过取
	# 如果是post请求，验证表单内容
	# regtisterForm 接受的是前端页面传来的表单信息
	if form.validate():
		return "success"
	return f'error:{form.errors}'


if __name__ == '__main__':
	app.run(debug=True)
# wtform

# 跨站脚本攻击 xss
# 指的是在一个网站的环境中注入恶意的html 包括附带的js
# 要防御这种攻击，开发者需要正确的转义文本，使其不能包含恶意的html标记
# 不让客户传HTML,JS
# 对文本进行正确的转义

# csrf 跨站请求伪造
# csrf_token

# Secret Key
# 对于每个要求修改服务器内容的请求，应该使用一次性的token，并存储在cookie里
# 并且在发送表单数据的同事附上他，在服务器再次接受数据之后，需要比较两个token
# 并确保相等

#### restful 设计规范 1 202075
