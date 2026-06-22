from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import date
from collections import defaultdict


class Employee(ABC):
    """Abstract base — every employee type must define how pay is calculated."""
    _id_counter = 1

    def __init__(self, name, department, base_salary):
        if base_salary < 0:
            raise ValueError("Base salary cannot be negative.")
        self.name           = name
        self._department    = department
        self.base_salary    = base_salary
        self.employee_id    = Employee._id_counter
        Employee._id_counter += 1
        self._hire_date     = date.today()

    @property
    def department(self):
        return self._department

    @department.setter
    def department(self, new_dept):
        if not new_dept.strip():
            raise ValueError("Department cannot be empty.")
        self._department = new_dept

    @abstractmethod
    def calculate_pay(self):
        pass

    @abstractmethod
    def get_role(self):
        pass

    def give_raise(self, amount):
        """Increase base_salary by amount. Must be positive."""
        if amount <= 0:
            raise ValueError("Raise amount must be positive.")
        self.base_salary += amount

    def get_payslip(self):
        return (
            f"#{self.employee_id} {self.name} ({self.get_role()}) — {self.department}\n"
            f"Pay: ${self.calculate_pay():,.2f}"
        )

    def __str__(self):
        return f"{self.get_role()}: {self.name} (${self.calculate_pay():,.2f})"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, department={self.department!r})"


class Manager(Employee):
    def __init__(self, name, department, base_salary, bonus, team_size=0):
        super().__init__(name, department, base_salary)
        self.bonus     = bonus
        self.team_size = team_size

    def calculate_pay(self):
        return self.base_salary + self.bonus

    def get_role(self):
        return "Manager"


class Salesperson(Employee):
    def __init__(self, name, department, base_salary, commission_rate, total_sales=0):
        super().__init__(name, department, base_salary)
        self.commission_rate = commission_rate
        self.total_sales     = total_sales

    def calculate_pay(self):
        return self.base_salary + (self.commission_rate * self.total_sales)

    def get_role(self):
        return "Salesperson"

    def record_sale(self, amount):
        if amount <= 0:
            raise ValueError("Sale amount must be positive.")
        self.total_sales += amount

class Developer(Employee):
    def __init__(self, name, department, base_salary, overtime_hours=0, overtime_rate=0):
        super().__init__(name, department, base_salary)
        self.overtime_hours = overtime_hours
        self.overtime_rate  = overtime_rate

    def calculate_pay(self):
        return self.base_salary + (self.overtime_hours * self.overtime_rate)

    def get_role(self):
        return "Developer"


class Intern(Employee):
    
    def __init__(self, name, department, base_salary, stipend):
        super().__init__(name, department, base_salary)
        self.stipend = stipend

    def calculate_pay(self):
        return self.stipend  # base_salary deliberately ignored

    def get_role(self):
        return "Intern"

    def give_raise(self, amount):
        """For interns, a raise increases the stipend, not base_salary."""
        if amount <= 0:
            raise ValueError("Raise amount must be positive.")
        self.stipend += amount

class Company:
    """Manages many employees — composition, same pattern as Bank/Account."""
    def __init__(self, name):
        self.name = name
        self._employees = []

    def hire(self, employee: Employee):
        self._employees.append(employee)
        return employee.employee_id

    def fire(self, employee_id):
        emp = self.find_employee(employee_id)
        if not emp:
            raise ValueError("Employee not found.")
        self._employees.remove(emp)
        return f"{emp.name} has been let go."

    def find_employee(self, employee_id):
        for emp in self._employees:
            if emp.employee_id == employee_id:
                return emp
        return None

    def total_payroll(self):
        return sum(emp.calculate_pay() for emp in self._employees)

    def employees_by_department(self, department):
        return [emp for emp in self._employees if emp.department == department]

    def average_salary_by_role(self):
  
        
        totals = defaultdict(float)
        counts = defaultdict(int)
        for emp in self._employees:
            role = emp.get_role()
            totals[role] += emp.calculate_pay()
            counts[role] += 1
        return {role: totals[role] / counts[role] for role in totals}

    def promote_to_manager(self, employee_id, bonus, team_size):
       
        emp = self.find_employee(employee_id)
        if not emp:
            raise ValueError(f"No employee with id {employee_id}.")
        self.fire(employee_id)
        new_manager = Manager(
            name         = emp.name,
            department   = emp.department,
            base_salary  = emp.base_salary,
            bonus        = bonus,
            team_size    = team_size,
        )
        self.hire(new_manager)
        return new_manager

    def __len__(self):
        return len(self._employees)

    def __iter__(self):
        return iter(self._employees)


# ── Test driver ──────────────────────────────────────────────────────────────

if __name__ == "__main__":
    company = Company("Acme Corp")

    # Hire one of each type
    mgr  = Manager    ("Diana Prince",  "Operations", 80_000, bonus=15_000, team_size=6)
    dev  = Developer  ("Bruce Wayne",   "Engineering", 95_000, overtime_hours=20, overtime_rate=75)
    rep  = Salesperson("Clark Kent",    "Sales",       45_000, commission_rate=0.08)
    intern_ = Intern  ("Diana Lance",   "Marketing",    0,     stipend=2_000)

    for emp in (mgr, dev, rep, intern_):
        company.hire(emp)

    # Record some sales for the salesperson
    rep.record_sale(50_000)
    rep.record_sale(30_000)

    print("=== Initial payslips ===")
    for emp in company:
        print(emp.get_payslip())
        print()

    # Give raises
    dev.give_raise(5_000)          # Developer: base_salary goes up
    rep.give_raise(3_000)          # Salesperson: base_salary goes up, commission unchanged
    intern_.give_raise(500)        # Intern: stipend goes up (overridden give_raise)

    print("=== After raises ===")
    for emp in company:
        print(emp)

    print()

    # Promote the salesperson to manager
    promoted = company.promote_to_manager(rep.employee_id, bonus=20_000, team_size=3)
    print(f"Promoted: {promoted}")
    print()

    # Average salary by role
    print("=== Average pay by role ===")
    for role, avg in company.average_salary_by_role().items():
        print(f"  {role}: ${avg:,.2f}")

    print()
    print(f"=== Full roster ({len(company)} employees) ===")
    for emp in company:
        print(f"  {emp}")

    print()
    print(f"Total payroll: ${company.total_payroll():,.2f}")