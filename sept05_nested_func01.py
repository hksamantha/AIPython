def find_largest(a,b,c):
    if a>b>c:
        return a
    elif a<b>c:
        return b
    else :
        return c

def cal_largest(func, a, b, c):
    return func(a, b, c)

result=cal_largest(find_largest, 3, 6,9)

print(result)