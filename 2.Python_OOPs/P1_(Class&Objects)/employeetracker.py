class Employee:
    company = "Techcorp"
    headcount = 0

    def __init__(self, name , department, salary):
        self.name = name
        self.department = department
        self.salary = salary
        Employee.headcount +=1

    def give_raise(self, amount):
        self.salary += amount

    def get_info(self):
        print(f"Company : {Employee.company}")
        print(f"Employee name is : {self.name}")
        print(f"Department : {self.department}")
        print(f"Salary : $ {self.salary:,.2f}")
    @classmethod
    def get_headcount(cls):
        return Employee.headcount
    
ashin = Employee("Ashin", "IT", 30000)
afsana = Employee("Afsana", "Marketing", 20000)
arslan = Employee("Arslan", "Finance", 50000)

ashin.get_info()
afsana.get_info()
arslan.get_info()
print(f"Total employees: {Employee.get_headcount()}")

    
