# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 007_cookie.py
@time: 2018/12/9 下午1:25
"""

from flask import  Flask,make_response,request

app = Flask(__name__)

@app.route("/set-cookie")
def set_cookie():
    resp = make_response("success")
    #设置cookie
    resp.set_cookie("Itcast","Python")
    resp.set_cookie("Itcast1", "Python1")

    resp.set_cookie("Itcast1", "Python1",max_age=3600)
    resp.headers["Set-Cookie"] =" Itcast2=Python1; Expires=Thu, 01-Jan-2019 00:00:00 GMT; Max-Age=3600; Path=/"
    return resp

@app.route("/get_cookie")
def get_cookie():
    c = request.cookies.get("Itcast")
    return c

@app.route("/delete_cookie")
def delete_cookie():
    resp = make_response('del success')
    resp.delete_cookie("Itcast1")
    return resp


if __name__ == '__main__':
    app.run(debug=True)

