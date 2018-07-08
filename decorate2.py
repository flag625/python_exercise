# -*- coding:utf-8 -*-
import functools

def log(func):
    def wrapper(*args,**kw):
        print('begin call %s():'%func.__name__)
        func(*args,**kw)
        print('end call %s():'%func.__name__)
        return func(*args,**kw)
    return wrapper

@log
def now():
    print('2017-09-14')
