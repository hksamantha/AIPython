n = int(input("Ennter a number: "))

if n <= 0:
    print("Please enter a positive number")
else:
    while n > 0:
        print('* '*n)
        n -= 1
