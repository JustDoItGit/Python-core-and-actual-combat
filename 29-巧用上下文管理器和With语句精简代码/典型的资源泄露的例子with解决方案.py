for x in range(10000000):
    with open('test.txt', 'w') as f:
        f.write('hello')

f = open('test.txt', 'w')
try:
    f.write('hello')
finally:
    f.close()
