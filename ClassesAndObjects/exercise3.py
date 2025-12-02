#Shared vs Unique Data

#Create a class Student where all students share a school_name (class variable),
# but each has their own name and grade.
# Print both shared and unique values.

class Student: 
    
    school = "Univesity Of Everyone"

    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 
    
    def student_details(self):
        return f"Student Name: {self.name} \n Grade: {self.grade} \n University: {Student.school}"


student1 = Student("John", 98)
student2 = Student("Tom", 88)
student3 = Student("Jeff", 80)

print(student1.student_details(), "\n")
print(student2.student_details(), "\n")
print(student3.student_details(), "\n")


