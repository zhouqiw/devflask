# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 10_flask_script.py
@time: 2018/12/9 下午7:09
"""

from flask import  Flask, render_template,request
from flask_script import Manager  #启动命令的管理类
app = Flask(__name__)

manager = Manager(app)


@app.route("/xss",methods=["GET","POST"])
def xss():
    text = ""
    if request.method == "POST":
        text = request.form.get("text")

    return render_template("xss.html",text = text)

if __name__ == '__main__':
    # app.run(debug=True)
    #通过管理对象来启动flask
    manager.run()