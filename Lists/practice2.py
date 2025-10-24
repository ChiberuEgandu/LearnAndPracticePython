"""
Print the students and there grades 
"""

def main():

    students = ["John", "Ed", "Tom", "Jeff"]
    
    grades = ["A", "B", "C-"]

    for student, grade in zip(students, grades):
        print(student, grade)

    print("\n")


    i = 0

    while i < len(student) and i < len(grades):
        print([i], students[i], grades[i])
        i += 1


if __name__ == '__main__':
    main()