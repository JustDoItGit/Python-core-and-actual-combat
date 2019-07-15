import functools


def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator1')
        func(*args, **kwargs)

    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('wrapper of decorator2')
        return func(*args, **kwargs)

    return wrapper


@my_decorator1
@my_decorator2
@my_decorator1
def greet(message):
    print(message)


greet('hello world')
