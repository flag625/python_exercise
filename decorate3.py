import functools

def log(arg):
    if not isinstance(arg, str):
        @functools.wraps(arg)
        def wrapper(*args,**kw):
            print('Begin call %s():'%arg.__name__)
            r = arg(*args,**kw)
            print('end call %s().'%arg.__name__)
            return r
        return wrapper
    else:
        def decorate(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print('%s %s():'%(arg,func.__name__))
                r = func(*args,**kw)
                print('end call %s().'%func.__name__)
                return r
            return wrapper
        return decorate

@log
def f1():
    print('1')

@log('execute')
def f2():
    print('2')