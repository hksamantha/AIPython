def smart_divide(func):
    def inner (a, b):
        print("I am goint for a division")
        if b==0:
            print("Whoops!, cannot divide")
            exit()
            return 
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    return a/b

print(divide(12, 4))