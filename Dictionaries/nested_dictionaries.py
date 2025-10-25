"""
Create a dictionary classroom with keys as student names and values as another dictionary containing "age" and "grade". Example structure:

classroom = {
    "Alice": {"age": 10, "grade": "A"},
    "Bob": {"age": 11, "grade": "B"}
}
Print each student's name and grade.
"""

def main():

    classroom = {
    "Alice": {"age": 10, "grade": "A"},
    "Bob": {"age": 11, "grade": "B"}
    }

    for key, value in classroom.items():
        print(key,value["grade"])

if __name__ == '__main__':
    main()