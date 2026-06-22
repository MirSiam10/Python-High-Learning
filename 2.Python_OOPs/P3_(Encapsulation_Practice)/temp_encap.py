class Temperature :

    def __init__(self, celsius):
        self.celsius = celsius
       
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, celsius):
        self._validate_celsius(celsius)
        self._celsius = celsius
    
    @property
    def farenheit(self):
        return (self._celsius * 9/5) + 32
    
    @property
    def kelvin(self):
        return (self._celsius + 273.15)
    

    @staticmethod
    def _validate_celsius(celsius):
        if not celsius > -273.15:
            raise ValueError("Invalid Value")
        

t1 = Temperature(100)
print(t1.celsius)
print(t1.farenheit)
print(t1.kelvin)

t1.celsius = 0
print(t1.farenheit)



try:
    t1.farenheit = 10
    t1.kelvin = 300

except AttributeError as e:
    print(f"{e}")