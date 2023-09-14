def personal_greeting(func):
    def inner():
        print("Hi admin")
        func()
    return inner

@personal_greeting
def normal_greeting():
    print("Hello how are you")


normal_greeting()