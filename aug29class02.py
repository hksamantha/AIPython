numbers = [10, 25, 37, 41, 58]

# This function will return remainder of a number divided by 3


def div(x):
    return x % 3


division3 = map(div, numbers)

print(list(division3))
