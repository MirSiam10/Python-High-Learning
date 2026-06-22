class Student:

    # _name    → property: must be non-empty string
    # _age     → property: must be int between 10 and 100
    # _gpa     → property: must be float 0.0–4.0
    # _courses → protected list: add via enroll(course)

    # _name    → property: must be non-empty string
    # _age     → property: must be int between 10 and 100
    # _gpa     → property: must be float 0.0–4.0
    # _courses → protected list: add via enroll(course)

     # enroll(course): adds to _courses if not already enrolled
    # drop(course):   removes from _courses if enrolled
    # get_info():     returns formatted string — all details
    # is_honor():     True if gpa >= 3.7

     # READ-ONLY properties:
    # course_count → returns len(_courses)
    # status       → "Honor Student" if gpa >= 3.7 else "Regular Student"


    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa
        self._courses = []

    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @property
    def gpa(self):
        return self._gpa
    
    @property
    def course_count(self):
        return len(self._courses)
    
    @name.setter
    def name(self, name):
     if not isinstance(name, str):
        raise TypeError("Name must be a string")

     if not name.strip():
        raise ValueError("Name cannot be empty")
     self._name = name   

    @age.setter
    def age(self, age):
        if not isinstance(age, int):
            raise TypeError("Age has to be an Integer")
        if age < 10 or age > 100:
            raise ValueError("Age must be int and between 10 and 100")
        self._age = age
    
    @gpa.setter
    def gpa(self, gpa):
        if not isinstance(gpa, float):
            raise TypeError("GPA must be float")
        if gpa <= 0.00 or gpa >= 4.00:
            raise ValueError("GPA must be between 0.00 - 4.00")
        self._gpa = float(gpa)
        

    
    @property
    def status(self):
        return "Honor Student" if self._gpa >= 3.75 else "Regular Student"
    



    def enroll(self, course):
        if course in self._courses:
            return f"{course} already enrolled"
        if not isinstance(course, str) or not course.strip():
            raise ValueError("Course must be a non-empty string")
        
        self._courses.append(course)
        return f"{course} added"
    

    def drop(self, course):
        if course in self._courses:
            self._courses.remove(course)

    
    def get_info(self):
        lines = [
            f"Name: {self.name}",
            f"Age: {self.age}",
            f"GPA: {self.gpa}",
            f"Course: {',' .join(self._courses)}",
            f"Status: {self.status}"
        ]
        return "\n".join(lines)
    

    def is_honor(self):
        """Return True if student's GPA qualifies for honors (>= 3.75)."""
        return self._gpa >= 3.75
    

s = Student("Ashin", 20, 3.85)
s.enroll("Math")
s.enroll("Physics")
s.enroll("Math")   # Already enrolled — should say so
s.drop("Physics")
s.enroll("ICT")

print(s.get_info())
print(s.is_honor())
print(s.course_count)

try:
    s.age = 200        # Should raise ValueError
except ValueError as e:
    print(e)

try:
    s.gpa = 5.0        # Should raise ValueError
except ValueError as e:
    print(e)
    