# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 10_flask_script.py
@time: 2018/12/9 下午7:09
"""

from flask import  Flask, render_template,request

app = Flask(__name__)




@app.route("/index")
def index():
    data = {
        "name": "python",
        "age": "18",
        "my_dict": {"city":"sz"},
        "my_list": [1,2,3,4,5],
        "my_int" : 0
    }

    return render_template("index.html",**data)


# 1 .自定义的过滤器
def list_step_2(list):
    """自定义的过滤器"""
    return list[::2]

#注册过滤器

app.add_template_filter(list_step_2,'li2')



# 2 .自定义的过滤器
@app.template_filter("li3")
def list_step_3(li):
    """自定义的过滤器"""
    return li[::3]


if __name__ == '__main__':
    app.run(debug=True)
