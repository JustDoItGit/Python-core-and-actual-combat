def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()

    return wrapper


def greet():
    print('hello world')


gre = my_decorator(greet)
gre()

greet = my_decorator(greet)
greet()
