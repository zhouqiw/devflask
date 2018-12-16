# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: 0001_wtf.py
@time: 2018/12/9 下午9:33
"""
from flask import  Flask,render_template,session,url_for,redirect,request,flash
from flask_wtf import FlaskForm
from wtforms import  StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired,EqualTo

app  = Flask(__name__)
app.config["SECRET_KEY"] = "xjsdlfjantsdfjasdkhfsd"

class RegisterForm(FlaskForm):
    """
     自定义的注册的表单模型类
    """
    #                         名字            验证器
    #DataRequired 保证数据必须填写，并且不能为空
    user_name = StringField(  label=u"用户名",  validators=[DataRequired(u"用户名不能为空")])
    password  = PasswordField(label=u"密码",    validators=[DataRequired(u"密码不能为空")])
    password2 = PasswordField(label=u"确认密码", validators=[DataRequired(u"确认密码不能为空"),EqualTo("password",u"两次密码不一致")])
    submit = SubmitField(label=u"提交")
    # user_name = StringField(label='username', validators=[DataRequired('username is not nil')])
    # password =  PasswordField(label='password', validators=[DataRequired('password is not nil')])
    # password2 = PasswordField(label='confirm password', validators=[DataRequired('confirm password is nil'), EqualTo('password', 'input password is diffient')])
    # submit = SubmitField(label='submit')


@app.route("/register",methods=["GET", "POST"])
def register():
    #创建一个对象,如果post请求，前端发送了数据。flask会把数据构造form对象的时候，存在到对象中
    form = RegisterForm()
    #判断form中的数据是否合理
    #如果form中的数据完全满足所有的验证，则返回为证，否则返回假
    if form.validate_on_submit():
        # 表示验证合格
        # 提取数据
        user_name = form.user_name.data
        pwd = form.password.data
        pwd2 = form.password2.data
        print(user_name,pwd,pwd2)
        session["user_name"] = user_name

        return redirect(url_for('index'))
    else:
        if request.method == 'POST':
            flash(u'输入有误！')
    return render_template("register.html",form=form)


@app.route("/index")
def index():
    user_name = session.get("user_name","")
    return "hi %s" % user_name

if __name__ == '__main__':
    app.run()