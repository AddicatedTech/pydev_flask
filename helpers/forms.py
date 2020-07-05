#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/5 0:34
# @Author  : Addicated
# @Site    : 
# @File    : forms.py
# @Software: PyCharm

# 表单验证模块
import re

from flask import session
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField,SelectMultipleField
from wtforms.validators import Regexp, DataRequired, Length, EqualTo, ValidationError


# 自定义验证器类
# 需要些一个init方法 一个call方法
# init 主要设置各种各样的实例属性，在下面的call方法中使用
# call 主要包含各种验证方法的编写
class Mobile:
	regex = re.compile(r"1[3,5,7,9]]\d{9}$")

	def __init__(self,message=None):
		if message is None:
			self.message = "不是手机号码"
		self.message = message

	def __call__(self, form, field):
		match = self.regex.match(field.data)
		if not match:
			message = self.message
			raise  ValidationError(message)
		return match
# class Exist:
# 	regex = re.compile(r"1[3,5,7,9]]\d{9}$")
#
# 	def __init__(self,message=None):
# 		if message is None:
# 			self.message = "不是手机号码"
# 		self.message = message
#
# 	def __call__(self, form, field):
# 		# 查询DB中是否已经存在，存在则抛异常
# 		# 否则return数据





class RegisterForm(FlaskForm):
	# 表单属性要和前端的input内容一致
	# 和数据库字段保持一致
	# 输入框 StringField
	# 密码输入 PasswordField
	# filed 第一个参数 widget（组件）
	# validators 默认是一个tup，一般来说使用列表格式传参，是验证器
	# Datarequeired()方法，对输入项进行非空判断，出错即抛异常，可传字符串信息作为提示语
	# Regexp 正则表达式验证器  同样可传msg作为提示 Length 长度验证 msg
	# Equal_to
	# RuntimeError: A secret key is required to use CSRF.
	# 只要使用wtforms组件就需要设置一个秘钥

	# error ： csrf_token': ['The CSRF token is missing.']}
	# 请求正常成功的情况下，F12中，查看headers里面，request headers 里面是有csrf_token的记载的
	# 前端页面中 在表单内    {{ form.hidden_tag() }}
	# get请求的时候将form对象传进去

	# filter 参数，传入一个可迭代对象，主要功能是对前端页面传来的信息
	# 进行一些额外的处理

	# render_kw 添加一些额外的属性进取，
	# 模板引擎的编写方式是在前端直接通过form对象去渲染
	# 或者是使用原生html代码
	# render_kw={'class':"form-control"} 前端F12会发现属于一个类
	# 名为 form-control

	# 默认值
	# filed内 default= 如果没有输入就默认为0，输入了，进行验证判断

	# 小结
	# form类 重要的函数
	# validate  验证主函数
	# process 验证数据，BaseForm里
	# errors 获取错误信息
	# form.data 在路由处编写逻辑时使用

	# 集中数据类型类
	# FloatField
	# DecimalField  必须输入数值，显示时保留一位小数 places
	# DateField 必须输入是 年-月-日 格式的日期

	# RedioField 单选框，choices里面内容会在ul标签中，
	# 实例 gender = RadioField('Gender',choices=[('m','Male'),("f","female")])
	# 每个项是 值，显示名  choices=[('m','Male')]

	# SelectField 下拉单选框，choices里面内容会在option，
	# job = SelectField('job',choices=[('IT','se'),("docor","aid")])
	# 每个项是 值，显示名  choices=[('m','Male')]

	# Select 类型，多选框 choices里面的内容会在option里面，里面每个项同上面的一样，
	# 值，显示名对
	# hobby = SelectMultipleField('hobby',choices=[('value','showname')])



	# 对应于html里面的元素，主要是通过form参数渲染模板，每一种不同的类型本质上还是一个
	# html格式的字符串的封装，放在widget属性里面

	# 几种常见的validate
	# DataRequired

	# --------------------------------------
	# 新一天的课
	# 自定义validator 用来满足复杂的验证
	# 需求，验证输入项是否为手机号码
	# 参见上面的 mobile类

	# 全局变量
	# 中间件  在流程中间进行一些额外的处理
	# flask 中成为钩子
	# 请求钩子
	# before request
	# 在获取某一个请求之前可以做一些额外的事情

	# 需求场景，运营： 数据埋点，当用户访问的时候进行计数，通常来说放在缓存里面或者是db中
	# app.py下进行编辑
	# @app.before_request 下写钩子方法
	# # 在某个请求之前，就会在任何一个请求之前进行被装饰的钩子方法
	# 统计流量，签名之类的需求，或者进行验证
	#  比如在请求发送之前连接DB

	# after request 当某一个请求结束了之后要做的事情
	# @app.after_request
	# 场景：封装响应信息，组装响应对象
	# response参数必须传，return必须是一个response对象
	# 通常用来修改响应
	# 如果访问的视图出现错误，则不会调用

	# @app.teardown_request
	# 不管发不发生错误，都会被调用
	# 场景，如果一个正常的视图，应该使用afterrequest
	# teardownrequest是无论如何都需要被执行
	# 比如一些资源的释放， DB 连接之类

	#@app.before_first_request
	# 在所有请求之前执行，并且只执行一次

	# 全局变量
	# request 当flask应用处理请求时，会根据从wsgi服务器收到的环境创建一个
	# request对象，因为工作者（取决于服务器的线程，进程或者携程，
	# 一次只能处理一个请求，所以该请求期间，请求数据可被认为是该工作者的
	# 全局数据，flask对此使用术语，本地情景

	# g 变量
	# 用来同一个请求中共享数据使用，不同请求之间不共同
	# 主要是用来验证用户信息
	# 实例看app.py中定义

	# session
	# login之后 session['user'] = username
	# session 可以跨请求， 登出的时候移除session中保存的user信息即可
	# 比如在 before_request中进行session中是否含有用户信息的判定
	# session.get(key)
	# 可以对session进项相关设置
	# session_cookie_name  permannet_session_lifetime
	# 解析
	# 登录成功的时候 F12 network下 会多一个set-cookie的一个字段
	# sessionid就存放在里面
	# 而后再去访问其他页面会带上这个session字段
	# 浏览器---登录----服务器----设置session['user'] = xxx----返回给浏览器
	# 返回的变量名为set-cookie（可修改 返回给浏览器
	# 之后浏览器每次发送请求都会在cookie中添加sessionid


	phone = StringField(render_kw={'class':"form-control"},label="手机号码", validators=[
		Regexp(r'^1[3,5,7,8,9]\d{9}$', message="手机号码格式错误"),
		Mobile(message="手机号已经存在"),
		DataRequired("手机号码不能为空")])  #
	pwd = PasswordField(label="密码", validators=[
		Length(6, 32, message='长度不对'),
		DataRequired("密码不能为空")])
	confirm_pwd = PasswordField(validators=[
		EqualTo('pwd',message="确认密码错误")])
	# webget可以通过form表单去渲染前端页面中


