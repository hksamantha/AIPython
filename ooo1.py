class Dog:

    #class attribute
    attr1 = "mammal"

    #The constructor
    def __init__(self, name):
        self.name = name

    def display(self):
        print("My dog name is", self.name)

    def update(self, new_name):
        self.name = new_name
        self.display()
        #print("Dog's new name is", self.name)
        

dog_1 = Dog("Tommy") 

dog_2 = Dog("Robby") 

print(dog_1.name)

print(dog_1.__class__.attr1)