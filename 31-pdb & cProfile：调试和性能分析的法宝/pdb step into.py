import pdb


def func():
    print('enter func()')


a = 1
b = 2
pdb.set_trace()
func()
c = 3
print(a + b + c)
