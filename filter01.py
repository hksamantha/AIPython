numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def even_numbers(x):
    return x % 2 == 0


even_number_list = filter(even_numbers, numbers)

print(type(even_number_list))

print(list(even_number_list))
