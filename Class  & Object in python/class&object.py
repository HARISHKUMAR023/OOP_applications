class animal:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def  explation(self):
        print(f"the name is {self.name} it age is {self.age} ")

ani1=animal("dog",45)
ani1.explation()