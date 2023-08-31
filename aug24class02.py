def summation(*args):
    x = 0
    for arg in args:
        x += arg
    return x


print(summation(2, 3, 4, 5, 6, 7))


def max(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}={value}')


print(max(name="John", age=28, city="Colombo"))
