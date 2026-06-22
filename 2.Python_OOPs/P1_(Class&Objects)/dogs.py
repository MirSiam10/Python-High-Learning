class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        return(f"{self.name} is a {self.breed} and says: Woof!")

buddy = Dog("Buddy", "Golden Retriever")
print(buddy.bark())
charlie = Dog("Charlie", "Labrador Retriever")
print(charlie.bark())
