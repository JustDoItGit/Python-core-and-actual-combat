import sys

a = []

# 两次引用，一次来自 a, 一次来自 getrefcount
print(sys.getrefcount(a))


def func(a):
    # 四次引用， a, python 的函数调用栈，函数参数，和getrefcount
    print(sys.getrefcount(a))


func(a)
# 两次引用，一次来自 a, 一次来自 getrefcount， 函数 func 调用已经不存在
print(sys.getrefcount(a))
