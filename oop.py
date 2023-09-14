class Dog:

    #The constructor
    def __init__(self, name):
        self.name = name

    def display(self):
        print("My dog's name is:", self.name)

    def update(self, new_name):
        self.name=new_name
        print("Dog's new name is", self.name)

dog_1 = Dog("Tommy") 

dog_1.display()
dog_1.update("Robby")
