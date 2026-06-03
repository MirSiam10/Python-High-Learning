class Student:
    def __init__(self, name, grade):
        self.name = name

        if 0 <= grade <= 100:
         self.grade = grade
        else:
           print("Grade must be in 0 to 100")
           self.grade = 0
#Method to get letter grade
    def get_letter_grade(self):
       
        if self.grade >= 90 :
            return "A"
        elif self.grade >= 80:
           return "B"
        elif self.grade >= 70:
           return "C"
        elif self.grade >= 60:
           return "D"
        else:
           return "F"
#Method to check if the student is passing
    def is_passing(self):
       if self.grade >= 60:
          return True
       else:
          return False
       
#Creating Student Objects
ashin = Student("Ashin", 90)
arsalan = Student("Arsalan", 80)
afsana = Student("Afsana", 45)

#Methods Called
print(f"{ashin.name}'s result is : {ashin.get_letter_grade()} and Passed: {ashin.is_passing()}")
arsalan.get_letter_grade()
print(f"{arsalan.name}'s result is : {arsalan.get_letter_grade()} and Passed: {arsalan.is_passing()}")
afsana.get_letter_grade()
print(f"{afsana.name}'s result is : {afsana.get_letter_grade()} and Passed: {afsana.is_passing()}")