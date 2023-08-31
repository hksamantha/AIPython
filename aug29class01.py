numbers = [1, 2, 3, 4, 5]


def square(x):
    return x**2


square_numbers = map(square, numbers)

print(list(square_numbers))
