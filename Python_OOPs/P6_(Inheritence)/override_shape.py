class Shape():
    def __init__(self, color):
        self.color = color
    def describe(self):
        return f"A {self.color}"
    
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius
    
    def describe(self):
        base_color =  super().describe()
        return f"{base_color} Circle with radius = {self.radius}"
    
class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side
    
    def describe(self):
        base_color =  super().describe()
        return f"{base_color} Square with side = {self.side}"
    
    #Polymorphism Format

shapes = [

            Circle("RED",2),
            Square("BLUE", 5)
]

for shape in shapes:
    print(shape.describe())