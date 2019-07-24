import sys

a = []

print(sys.getrefcount(a))  # 两次，getrefcount 引用时 +1， 引用结束 -1

b = a

print(sys.getrefcount(a))  # 3次

c = b
d = b
e = c
f = e
g = d

print(sys.getrefcount(a))  # 8次
