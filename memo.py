#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 8:41
# @Author  : Addicated
# @Site    : 
# @File    : memo.py
# @Software: PyCharm

# orm框架学习 2020.7.8
# 进度统计 6.10~7.8 目前59/120
# 粗计 28days 完成一半流程，到8月初完成整个学习

# 什么是orm
# 学习成本高，但是性能比不上原生
# 提高开发效率，元编程概念。

# current_app
# sqlite的使用
# python自带sqlite3
# 小巧功能较为强大，百万级
# 不要联网 demo.db 只有一个文件方便做数据迁移
# 测试平台，单机小游戏
# 编程模式
# 原生 sql 谁都读得懂，维护成本，开发效率低
# orm 1，sql ，2，可读性
# orm
# 什么是orm 类和对象封装
# 1，学习成本非常高，性能
# 2，开发效率高
# 元编程

# 将pymysql 和sql语句封装成对象
# orm实际上就是关系映射对象，一层一层封装，将简单的sql查询进行了封装
# 可以通过类，属性，方法的方式映射sql语句进行调用

# 好处
# 避免sql注入， 各个不同的数据需要些不同的查询语言，这个不用

# 坏处
# 每一个具体的语法是不一样的，sql语句大体通用
# 学习成本高

# orm建表 vs 手工建表
# 查询操作 ，前提，表
# 手工建表，
# orm 先代码，通过代码自动生成表结构
# code first风格
# 数据库创建步骤
# 先安装flask sqlalchemy  通用 django ，toroto flask
# 1 配置DB  mysql or sqlite
# 2 定义表结构，设计表
# 3 创建表
# 使用步骤见 app1

#  orm框架学习2  2020.7.8

# 电商凭条买东西
# 1，选择对应的商品，订单
# 2，加入购物车

# 支付 事务
# 3， 支付，微信
#    1，支付状态 改成before_pay
#    2, 微信-> before_weixin
#    3, 微信-> zhengzai_weixin
#    4, success / error
#    5, 完成