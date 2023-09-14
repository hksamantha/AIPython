def smart_fact(func):
    def inner(n):
        if n<0:
            print("negative number")
            return
        return func(n)
    return inner


@smart_fact
def cal_fact(n):
    fact=1
    for i in range(1, n+1):
        fact=fact*i
    print(fact) 

cal_fact(-2)

