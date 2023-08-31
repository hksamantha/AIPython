def myfunc(n):
    return lambda a: a*n

my_doubler=myfunc(2) # lambda a : a*2

new_value= my_doubler(10) # lambda 10: 10*2=20



