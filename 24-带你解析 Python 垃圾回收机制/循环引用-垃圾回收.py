import os
import gc
import psutil


# 显示当前 Python 程序占用内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))


def func():
    show_memory_info('initial')
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a created')
    a.append(b)
    b.append(a)


func()
gc.collect()
show_memory_info('finished')
