# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: url_demo.py
@time: 2018/12/8 上午10:14
"""
from flask import  Flask, url_for,redirect
from werkzeug.routing import  BaseConverter

app = Flask(__name__)

@app.route("/goods/<int:goods_id>")
def goods_detail(goods_id):

    return "goods detail page %s" % goods_id

# 1.定义自己的转换器

class MobileConverter(BaseConverter):
    def __init__(self,url_map):
        super(MobileConverter,self).__init__(url_map)
        self.regex= r'1[345789]\d{9}'




class RegexConverter(BaseConverter):
    """"""
    def __init__(self,url_map,regex):
        #调用父类的初始化方法
        super(RegexConverter,self).__init__(url_map)
        #将正则表达式的参数保存到对象的属性中。flask会去使用这个属性来进行路由正则匹配
        self.regex =regex


    def to_python(self, value):
        print('to_python is runing!')
        return value

    def to_url(self, value):
        print('to_url function is runing')
        return  value



# 2.将自定义的转换器添加到flask的应用中
app.url_map.converters["re"] = RegexConverter
app.url_map.converters['mobile']=MobileConverter

#127.0.0.1:500/send/1869999904
@app.route("/send/<re(r'1[345789]\d{9}'):mobile>")
def send_sms(mobile):
    return "send sms to %s" % mobile


@app.route("/sends/<mobile:mobile_num>")
def send_smss(mobile_num):
    return "send sms to %s" % mobile_num


@app.route("/index")
def index():
    url = url_for('send_sms', mobile = "13499992222")
    return redirect(url)

if __name__ == '__main__':
    app.run(debug=True)