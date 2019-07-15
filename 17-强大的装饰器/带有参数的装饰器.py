def my_decorator(func):
    def wrapper(message):
        print('wrapper of decorator')
        func(message)

    return wrapper


@my_decorator
def greet(message):
    print(message)


greet('hello world')
