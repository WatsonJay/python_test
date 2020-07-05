# -*- coding: utf-8 -*-
# @Time    : 2020/6/15 11:28
# @Author  : Jaywatson
# @File    : decorator.py
# @Soft    : python_test
from functools import wraps

def new_decorator(a_func):

    @wraps(a_func)
    def warpTheFunction():
        print("before function")

        a_func()

        print("after function")

    return warpTheFunction

@new_decorator
def test_function():
    print("in function")


if __name__ == '__main__':
    test_function()
    print(test_function.__name__)