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
           print(f"{self.name} got A")
        elif self.grade >= 80:
           print(f"{self.name} got B")
        elif self.grade >= 70:
           print(f"{self.name} got C")
        elif self.grade >= 60:
           print(f"{self.name} got D")
        # elif self.grade >= 50:
        #    print(f"{self.name} got F")
        else:
           print(f"{self.name} Failed")
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
ashin.get_letter_grade()
print(f"{ashin.name} is passing: {ashin.is_passing()}")
arsalan.get_letter_grade()
print(f"{arsalan.name} is passing: {arsalan.is_passing()}")
afsana.get_letter_grade()
print(f"{afsana.name} is passing: {afsana.is_passing()}")