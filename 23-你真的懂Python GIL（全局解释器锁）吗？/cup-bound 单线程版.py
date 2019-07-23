import time


def CountDown(n):
    while n > 0:
        n -= 1


start_time = time.perf_counter()
CountDown(100000000)
end_time = time.perf_counter()
print(end_time - start_time)
