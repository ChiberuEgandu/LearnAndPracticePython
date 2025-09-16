#Exersise 6: Grade Calculator
#Write a function get_grade(score) that:
#Returns "A" if score ≥ 90
#"B" if score ≥ 80
#"C" if score ≥ 70
#"D" if score ≥ 60
#"F" otherwise

def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
print(get_grade(90))

def main():
    print(get_grade(90))
    print(get_grade(80))
    print(get_grade(70))
    print(get_grade(60))
    print(get_grade(50))

main()