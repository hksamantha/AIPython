a = [10, 23, 56, 78]
b = tuple(a)
a[3] = 95
a[1] = 34

print(b)
print(list(a))
