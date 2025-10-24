"""
1.Create a simple dictionary
Create a dictionary called student with keys: "name", "age", and "grade", and 
assign them any values you like. Print the dictionary.

2. Access values
Using the dictionary from Exercise 1, print only the "name" and "grade" of the student.

3.Add a new key-value pair
Add a key "city" to the student dictionary and assign it a value. Print the updated dictionary.

4.Update a value
Update the "grade" of the student to a new value. Print the updated dictionary.


5.Check for a key
Write a program that checks if the key "age" exists in the student dictionary. 
Print "Yes" if it exists, "No" if it doesn't.

"""

def main():
    #1.
    students  = {
        "name": "John",
        "age": 28,
        "grade": "A"
    }
    #2
    print(students)
    print(students["name"], students["grade"])

    #3
    students["city"] = "Arua"
    print(students)

    #4
    students["grade"] = "B"
    print(students)

    #5
    if "age" in students:
        print("Yes")
    else:
        print("No")


    
if __name__ == '__main__':
    main()