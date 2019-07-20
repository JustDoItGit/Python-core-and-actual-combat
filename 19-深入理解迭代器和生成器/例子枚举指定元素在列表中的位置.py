def index_normal(L, target):
    result = []
    for i, num in enumerate(L):
        if num == target:
            result.append(i)
    return result


print(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2))


def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i


print(list(index_normal([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)))
