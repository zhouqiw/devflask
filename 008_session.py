# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 008_session.py
@time: 2018/12/9 下午3:46
"""

from flask import  Flask,request,url_for

app = Flask(__name__)

@app.route("/index")
def index():
    print("index runing")
    return "index page"


@app.route("/hi")
def hi():
    print("hi runing")
    return "hi page"


@app.before_first_request
def handle_before_first_request():
    """每次请求都会被执行"""

    print("handle_before_first_request runed")

@app.before_request
def handle_before_request():
    """在每次请求之前被执行，前提是视图函数没有出现异常
    """
    print("handle_before_request be ex..ed")

@app.after_request
def handle_after_request(response):
    """在每次请求（视图函数处理）之后都被执行，前提是视图函数没有出现异常"""
    print("handl_after_request be excued")
    return response

@app.teardown_request
def handle_tesrdown_request(response):
    """在每次请求之后都被执行，无论视图韩式是否出现异常，都执行"""

    print(request.path)
    path = request.path
    print(url_for('index'))
    if path == url_for('index'):
        print("index 的请求")
    elif path == url_for('hi'):
        print("hi  的请求")

    print("handle_tesrdown_request be ex..ed")

    return response



if __name__ == '__main__':
    app.run(debug=True)

