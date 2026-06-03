class Circle:
    PI = 3.14159
    count = 0

    def __init__(self, radius):
        self.radius = radius
        Circle.count += 1

    def area(self):
        return f"The area is {Circle.PI * self.radius**2} "
    
    def circumference(self):
        return f"The circumference is : {2* Circle.PI * self.radius}"

    def get_count(self):
        return Circle.count

circle1 = Circle(3)
circle2 = Circle(5)

print(circle1.area())
print(circle1.circumference())
print(f"X circles created so far : {circle1.get_count()}")

print(circle2.area())
print(circle2.circumference())
print(f"X circles created so far : {circle2.get_count()}")
    

