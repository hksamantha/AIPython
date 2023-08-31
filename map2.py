numbers_1 = [1, 2, 3]
numbers_2 = [10, 20, 30]


def multiplication(x, y=5):
    return x*y


# In map() we can call numers_1 and numbers_2 as well
multi_list = list(map(multiplication, numbers_1))

print(multi_list)
