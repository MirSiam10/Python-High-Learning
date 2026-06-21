class Vehicle:
    def __init__(self, brand, speed):
            self.brand = brand
            self.speed = speed
    def move(self):
          return f"{self.brand} Moves at {self.speed} km/h"

class Car(Vehicle):
      def __init__(self, brand, speed, num_doors):
            super().__init__(brand, speed)
            self.num_doors =num_doors
      def move(self):
        base_move = super().move()
        return f"{base_move} and has {self.num_doors} Num Doors"

class Motorcycle(Vehicle):
      def __init__(self, brand, speed, side_cars):
            super().__init__(brand, speed)
            self.side_cars =side_cars

      def move(self):
        base_move = super().move()
        return f"{base_move} and has {self.side_cars} Side Cars"
      
peep = Car("Ferrari", "570", "2")
vroom = Motorcycle("BMW", "1000", "2")

print(peep.move())
print(vroom.move())