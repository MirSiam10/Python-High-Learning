class Cat:
    def speak(self):
        return "Meow"
    
class Dog:
    def speak(self):
        return "Woof"

class Duck:
    def speak(self):
        return "Quack"
    
def animal_chorus(animals):
    for animal in animals:
        print(animal.speak())

animals = [Cat(), Dog(), Duck(), Cat()]
(animal_chorus(animals))