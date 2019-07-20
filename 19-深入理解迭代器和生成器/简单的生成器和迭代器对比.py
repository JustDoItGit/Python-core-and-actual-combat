import os
import time
import psutil


def cost_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('cost time: {}s'.format(end - start))
        return res

    return wrapper


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024.0 / 1024
    print('{} memory used: {} MB'.format(hint, memory))


@cost_time
def tst_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(10000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    # 迭代器里的内容可以重复使用
    print(sum(list_1))
    show_memory_info('after sum called')


@cost_time
def tst_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(10000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    # 生成器里的对象用完就销毁了
    print(sum(list_2))
    show_memory_info('after sum called')


tst_iterator()
tst_generator()
