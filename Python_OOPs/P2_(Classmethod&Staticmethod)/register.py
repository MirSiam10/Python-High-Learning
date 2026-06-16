class Student:
    school = "DIU"          # Class variable
    _students = []          # Tracks ALL student objects

    def __init__(self, name, subject, gpa):
        if not Student.validate_gpa(gpa):
            raise ValueError("GPA must be between 0.0 and 4.0")

        self.name = name
        self.subject = subject
        self.gpa = gpa

    def register(self):
        Student._students.append(self)

    def get_info(self):
        return (f"Name: {self.name}, "
                f"Subject: {self.subject}, "
                f"GPA: {self.gpa}, "
                f"School: {Student.school}")

    def is_honor_student(self):
        return self.gpa >= 3.7

    @classmethod
    def get_all_students(cls):
        return [student.name for student in cls._students]

    @classmethod
    def get_honor_students(cls):
        return [student.name for student in cls._students
                if student.gpa >= 3.7]

    @classmethod
    def get_school_summary(cls):
        return f"School: {cls.school}, Total Students: {len(cls._students)}"

    @staticmethod
    def validate_gpa(gpa):
        return 0.0 <= gpa <= 4.0


s1 = Student("Siam", "CSE", 3.85)
s2 = Student("Rahim", "EEE", 3.20)
s3 = Student("Karim", "CSE", 3.90)

s1.register()
s2.register()
s3.register()

print(s1.get_info())
print(s2.is_honor_student())

print(Student.get_all_students())
print(Student.get_honor_students())
print(Student.get_school_summary())
