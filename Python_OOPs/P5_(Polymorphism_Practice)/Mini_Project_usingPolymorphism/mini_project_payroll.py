class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_pay(self):
        return self.base_salary

    def get_payslip(self):
        return (
            f"Employee: {self.name}\n"
            f"Pay: ${self.calculate_pay():,.2f}"
        )


class Manager(Employee):
    def __init__(self, name, base_salary, bonus):
        super().__init__(name, base_salary)
        self.bonus = bonus

    def calculate_pay(self):
        return self.base_salary + self.bonus


class Salesperson(Employee):
    def __init__(self, name, base_salary, commission_rate, total_sales):
        super().__init__(name, base_salary)
        self.commission_rate = commission_rate
        self.total_sales = total_sales

    def calculate_pay(self):
        return self.base_salary + (
            self.commission_rate * self.total_sales
        )


class Intern(Employee):
    def __init__(self, name, base_salary, stipend):
        super().__init__(name, base_salary)
        self.stipend = stipend

    def calculate_pay(self):
        return self.stipend


def total_payroll(staff):
    total = 0
    for employee in staff:
        total += employee.calculate_pay()
    return total


# Create employees
manager = Manager("Alice", 5000, 1500)
salesperson = Salesperson("Bob", 3000, 0.10, 20000)
intern = Intern("Charlie", 1000, 800)

# Single list
staff = [manager, salesperson, intern]

# Polymorphism test
for employee in staff:
    print(employee.get_payslip())
    print("-" * 30)

# Total payroll
print(f"Total Payroll: ${total_payroll(staff):,.2f}")