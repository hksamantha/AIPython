def myfunc(n):
    return lambda a: a*n

my_tripler=myfunc(3)

new_value=my_tripler(10)

print(new_value)