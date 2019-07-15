def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent

    return exponent_of


square = nth_power(2)  # 计算一个数的平方
cube = nth_power(3)  # 计算一个数的立方

print(square(2))
print(square(3))


# 不使用闭包
def nth_power_rewrite(base, exponent):
    return base ** exponent


print(nth_power_rewrite(2, 2))
print(nth_power_rewrite(3, 2))
