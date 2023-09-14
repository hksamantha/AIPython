class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")



dog_1 = Dog("Tommy")
dog_1.speak()

cat_1 = Cat("Kitty")
cat_1.speak()