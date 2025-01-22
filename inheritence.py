class SuperClass1:
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass2, SuperClass1):
    pass

d1 = Derived()
d1.info()  

# Output: "Super Class 1 method called"