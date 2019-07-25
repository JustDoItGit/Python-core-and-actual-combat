import cProfile


def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def fib_seq(n):
    res = []
    if n > 0:
        res.append(fib_seq(n - 1))
    res.append(fib(n))
    return res


# fib_seq(30)
cProfile.run('fib_seq(30)')
