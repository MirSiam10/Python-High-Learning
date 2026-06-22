class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

class Duck:
    def speak(self):
        return "Quack"

class Robot:
    def speak(self):
        return "BEEP BOOP"

class Rock:
    pass


def animal_chorus(things):
    for obj in things:
        if hasattr(obj, "speak"):
            print(f"{type(obj).__name__} says: {obj.speak()}")
        else:
            print(f"{type(obj).__name__} can't speak.")


things = [Cat(), Dog(), Duck(), Robot(), Rock()]
animal_chorus(things)