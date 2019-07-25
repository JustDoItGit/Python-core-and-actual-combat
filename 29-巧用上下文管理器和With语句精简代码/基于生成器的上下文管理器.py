from contextlib import contextmanager


@contextmanager
def file_manager(name, mode):
    global f
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()


with file_manager('test.txt', 'w') as f:
    f.write('hello world')
