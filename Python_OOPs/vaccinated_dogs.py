class VaccinatedDogs:

    def __init__(self, name, breed, age, is_vaccinated=False):
        self.name          = name
        self.breed         = breed
        self.age           = age
        self.is_vaccinated = is_vaccinated   # defaults to False

    def describe(self):
        status = "vaccinated" if self.is_vaccinated else "not vaccinated"
        print(f"{self.name} | {self.breed} | Age: {self.age} | {status}")


dog1 = VaccinatedDogs("Bruno", "Labrador", 3)               # uses default
dog2 = VaccinatedDogs("Milo",  "Poodle",   5, True)         # overrides default
dog3 = VaccinatedDogs("Rex",   "Husky",    2, is_vaccinated=True)  # explicit keyword

dog1.describe()  # Bruno | Labrador | Age: 3 | not vaccinated
dog2.describe()  # Milo  | Poodle   | Age: 5 | vaccinated
dog3.describe()  # Rex   | Husky    | Age: 2 | vaccinated