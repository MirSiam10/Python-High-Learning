class Temperature :
    def __init__(self, celsius):
        self.celsius = celsius

    def to_farenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return (self.celsius + 273.15)

    @classmethod
    def from_farenheit(cls, f):
        celsius = (f - 32)*5/9
        return cls(celsius)

    @classmethod
    def from_kelvin(cls, k):
        celsius = k - 273.15
        return cls(celsius)

    @staticmethod
    def is_valid(celsius):
        return celsius >= -273.15
        
temp1 = Temperature(100)
temp2 = Temperature.from_farenheit(32)
temp3 = Temperature.from_kelvin(373.15) 

print(temp1.celsius)
print(temp1.to_farenheit())
print(temp2.celsius)
print(temp3.celsius)
print(Temperature.is_valid(-300))
print(Temperature.is_valid(100))