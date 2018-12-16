# encoding: utf-8

"""
@author: zhouqi
@software: PyCharm
@file: use_with_methed.py
@time: 2018/12/9 上午8:46
"""

class Foo(object):
    def __enter__(self):
        """进入with语句的时候被with调用"""
        print("enter called")

    def __exit__(self, exc_type, exc_val, exc_tb):
        """离开with语句的时候被with调用"""
        print("exit called")
        print("exc_type: %s" % exc_type)
        print("exc_val: %s" % exc_val)
        print("exc_tb: %s" % exc_tb)


with Foo() as foo:
    print("hello python")
