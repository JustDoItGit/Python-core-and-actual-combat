import dis
import threading

n = 0
lock = threading.Lock()

def foo():
    global n
    with lock:
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
print(dis.dis(foo))
