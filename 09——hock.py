# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 008_session.py
@time: 2018/12/9 下午3:46
"""

from flask import  Flask,session

app = Flask(__name__)

#flask的session需要用到的秘钥字符串
app.config["SECRET_KEY"] = "jsldjflsadjlgjsdljfljlsdfasg"


#flask默认的把

@app.route("/login")
def login():
    session["name"]   = "Python"
    session["mobile"] = "18611119999"
    return "login success"


@app.route("/index")
def index():
    name = session.get("name")
    return "hello %s" % name


if __name__ == '__main__':
    app.run(debug=True)

