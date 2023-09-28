class Person:
    def __init__(self, name, idnumber):
        self.name=name
        self.idnumber=idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

    def details(self):
        print("My Name is", self.name)
        print("IdNumber", self.idnumber)

class employee(Person):
    def __init__(self, name, idnumber, post, salary):
        super().__init__(name, idnumber)
        self.post=post
        self.salary=salary

    
    def display(self):
        super().display() # This equal to Person.display(self)
        print(self.post)
        print(self.salary)

    def details(self):
        super().details() # This equal to Person.detalis(self)
        print("My Post is", self.post)
        print("Salary", self.salary)
employee_1=employee("Jan", 12345, "Engineer", 50000)

employee_1.display()
employee_1.details()
    



