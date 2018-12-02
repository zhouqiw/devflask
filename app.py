# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: app.py
@time: 2018/12/2 下午3:49
"""
from flask import  Flask
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import  UserMixin

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:example.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'mysecret'

db = SQLAlchemy(app)

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))

class MyModelView(ModelView):
    pass


admin = Admin(app)
admin.add_view(ModelView(User,  db.session))


if __name__ == '__main__':
    app.run(debug=True, port= 8080)