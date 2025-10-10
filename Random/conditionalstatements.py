#Thirty days hath September, April, June, and Novembe
#All the rest have 31, excepting February alone.
#def main():
#month = input("Enter month: ")
# determine the number of days
#if month == "Feb":
#days = 28
#elif month == "Sep" or month == "Apr" or month == "Jun" or month == "Nov":
#days = 30
#else:
#days = 31
#print(month, "has", days, "days")
#main()


month = input("Please provide a month with firt three letters: ")

while month not in ["jan", "feb", "mar", "apr", "may", "jun",
                "jul", "aug", "sep", "oct", "nov", "dec","Jan",
                "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
                "JAN", "FEB", "MAR", "APR", "MAY", "JUN","JUL", "AUG", "SEP", "OCT", "NOV", "DEC"]:
    month = input("INVALID INPUT. Must be 3 letters and a valid month. Try again: ")


if month == "Feb" or month == "FEB":
    days = 28
elif month == ["Sep","Apr","Jun","Nov"] or month == ["SEP","APR","JUN","NOV"]:
    days = 30
else:
    days = 31

print(month, "has", days, "days")