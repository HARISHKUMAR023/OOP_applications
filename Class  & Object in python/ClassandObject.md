# Classes and Objects

### Classes
A class is like a blueprint for creating objects. It defines a set of attributes and methods that the created objects can have.

### Objects

An object is an instance of a class. When a class is defined, no memory is allocated until an object of that class is created.

### Python code for Create class and Object
``` python
class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def  explation(self):
        print(f"the name is {self.name} it age is {self.age} ")

ani1=animal("dog",45)
