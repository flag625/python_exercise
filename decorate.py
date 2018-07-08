import functools
def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args,**kw):
             print('%s %s():'%(text, func._name_))
             return func(*args,**kw)
        return wrapper
    return decorator


@log('execute')
def now():
    print('2017-09-14')
