# Multiple Inheritence

class Flyable:
    def fly(self):
        return f"{self.name } is flying"
    
class Swimmable:
    def swim(self):
        return f"{self.name} is swimming"
    
class Duck(Flyable, Swimmable):
    def __init__(self, name):
        self.name = name
    
d = Duck("Donald")

print(d.fly())
print(d.swim())