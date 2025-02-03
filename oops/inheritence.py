
class Animal:
    def __init__(self, name):
        self.name = name 

    def speak(self):
        pass  

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!" 

dog = Dog("Buddy")
print(dog.speak())  

print("------------------------ Method overriding ------------------------------------------------")
#------------------------------------------------------------------------------------------------------------


class Parent:
    def show(self):
        print("This is the parent class method.")

class Child(Parent):
    def show(self):  
        print("This is the child class method.")

c = Child()
c.show()  

#------------------------------------------------------------------------------------------------------------
print("------------------------ Operating overloading ------------------------------------------------")

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

   
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    

    def __mul__(self, other):
        return self.x * other.x + self.y * other.y
    

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2, 3)
v2 = Vector(4, 5)


v3 = v1 + v2
print(v3) 

v4 = v1 - v2
print(v4) 


dot_product = v1 * v2
print(dot_product) 
