def sum_marks(dict):
    total = 0
    for x in dict.values():
        total += x
        return total


marks = {
    "maths": 80,
    "physics": 90,
    "chemistry": 70,
    "english": 80
}


print(sum_marks(marks))
