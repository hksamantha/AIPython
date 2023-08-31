strings = ["1", "2", "3", "4", "5"]

def convert_to_int(x):
    return int(x)

new_list = list(map(convert_to_int, strings))

print(new_list)
