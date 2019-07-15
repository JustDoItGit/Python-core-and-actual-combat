def my_decorator(func):
    def wrapper(*args, **kwargs):
        print('wrapper of decorator')
        print('wrapper {}'.format(args[0]))
        func(*args, **kwargs)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')
