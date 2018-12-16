# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 10_flask_script.py
@time: 2018/12/9 下午7:09
"""

from flask import  Flask, request, render_template


app = Flask(__name__)


text = []

@app.route("/xss",methods=["GET","POST"])
def xss():
    global text
    if request.method == "POST":
        text .append(request.form.get("text"))

    return render_template("xss.html",text = text)


if __name__ == '__main__':
    app.run(debug=True)
