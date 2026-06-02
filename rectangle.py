class Rectangle :
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        if self.width == self.height:
            return True
        else:
            return False

    def description(self):
        return f"Rectangle: {self.width}*{self.height}. Area = {self.area()}, Perimeter = {self.perimeter()} "
    
rectangle = Rectangle(4,6)
print(f"Area of rectangle is : {rectangle.area()}")
print(f"Perimeter of rectangle is : {rectangle.perimeter()}")
print(f"Is square: {rectangle.is_square()}")
print(rectangle.description())





