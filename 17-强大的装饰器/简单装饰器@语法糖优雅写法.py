def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


@my_decorator
def greet():
    print('hello world')


greet()
