# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: __init__.py
@time: 2018/12/2 下午5:34
"""

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models