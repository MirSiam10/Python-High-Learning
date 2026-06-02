class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def name_and_breed(self):
        print(f"{self.name} is a {self.breed}.")

Buddy = Dog("Buddy", "Golden Retriever")
Buddy.name_and_breed()
Charlie = Dog("Charlie", "Labrador Retriever")
Charlie.name_and_breed()