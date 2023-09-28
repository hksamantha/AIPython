class MyClass:
    def __init__(self):
        self._protected_var=20 # one underscor is protected variable
        self.__private_var=10  # two underscore means private variable

    
def display_something(self):
       print("display_something")

def __display_something_private(self):
       print("display_something_private")

obj = MyClass()
print(obj._protected_var)  # Accessing protected attribute
#print(obj.__private_var)  # Error: AttributeError - Cannot access private attribute directly

#obj.display_something()

#obj.__display_something()

def get_private_value(self):
       print(self.__private_var)

def set_private_value(self, New_value):
    self.__private_var=New_value
    print(self.__private_var)
obj.set_private_value(25)
obj.get_private_value()
