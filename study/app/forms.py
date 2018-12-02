# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: forms.py
@time: 2018/12/2 下午5:56
"""

from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(Form):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remember_me', default=False)