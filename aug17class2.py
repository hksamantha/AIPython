x = int(input("Enter your no: "))
fac = 1
if x < 0:
    print("please enter + number")
if x == 0:
    print(fac)
else:
    for i in range(1, x+1):
        fac *= i
print(fac)
