from abc import ABC, abstractmethod
class Vehicle(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def fuel_type(self):
        pass

    def get_info(self):
        return (
            f"This car's brand is : {self.brand}\n"
            f"Model is : {self.model}\n"
            f"start engine : {self.start_engine()}\n"
            f"Fuel type : {self.fuel_type()}"
                )
    
class ElectricCar(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start_engine(self):
        return "Silent start - electric motor engaged"
    
    def fuel_type(self):
        return "Electric"
    
class PetrolCar(Vehicle):
    def __init__(self, brand, model):
        super().__init__(brand, model)

    def start_engine(self):
        return "Vroom! Engine ignited"
    
    def fuel_type(self):
        return "Petrol"
    
ev = ElectricCar("Tesla", "Model 3")
gas = PetrolCar("Toyota", "Corolla")
print(ev.get_info())
print()
print(gas.get_info())