class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} is a {self.breed} and says: Woof!")

Buddy = Dog("Buddy", "Golden Retriever")
Buddy.bark()
Charlie = Dog("Charlie", "Labrador Retriever")
Charlie.bark()