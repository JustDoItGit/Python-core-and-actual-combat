import threading

n = 0


def foo():
    global n
    n += 1


# 下面代码明显对n线程不安全
threads = []
for i in range(100):
    t = threading.Thread(target=foo)
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print(n)
