from abc import ABC , abstractmethod

class Employee(ABC):
    def __init__(self, name, employe_id):
        self.name = name
        self.employe_id = employe_id

    @abstractmethod
    def calculate_salary(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def get_pay_slip(self):
       return( 
        f"Employe : {self.name} ({self.employe_id})\n"
        f"Role : {self.get_role()}\n"
        f"Salary : $ {self.calculate_salary():,.2f}"
       )

class FulltimeEmploye(Employee):

    def __init__(self, name, employe_id, annual_salary):
        super().__init__(name, employe_id)
        self.annual_salary = annual_salary

    def calculate_salary(self):
            return self.annual_salary / 12
        
    def get_role(self):
        return "Full Time Employe"
    
class ContractEmploye(Employee):
    def __init__(self, name , employe_id, hourly_rate, hours_worked):
        super().__init__(name, employe_id)
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked

    def calculate_salary(self):
        return self.hourly_rate * self.hours_worked
    
    def get_role(self):
        return "Contracted Employe"
    
emp1 = FulltimeEmploye("Ashin", "DKI307", 60000)
emp2 = ContractEmploye("Afsana", "DKI310", 20, 20)

print(emp1.get_pay_slip())
print()
print(emp2.get_pay_slip())