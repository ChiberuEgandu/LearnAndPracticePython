"""

find the min temp from this list 
HIGH_TEMPS = [92, 84, 98, 87, 94, 86, 75, 81, 91, 96, 75,
74, 78, 78, 76, 79, 77, 91, 83, 77, 79, 74,
78, 86, 88, 87, 84, 82, 82, 81, 83]
"""

def main():

    HIGH_TEMPS = [92, 84, 98, 87, 94, 86, 75, 81, 91, 96, 75,
                74, 78, 78, 76, 79, 77, 91, 83, 77, 79, 74,
                78, 86, 88, 87, 84, 82, 82, 81, 83]
    
    #using while loop 

    minimum_temp = HIGH_TEMPS[0]
    print(minimum_temp)
    i = 0

    while i < len(HIGH_TEMPS):
        if HIGH_TEMPS[i] < minimum_temp:
            minimum_temp = HIGH_TEMPS[i]
        i += 1
    print(f"The minimum temp from the list of numbers  {minimum_temp} ")


    # min high temp in July
    min_temp = 92
    for temp in HIGH_TEMPS:
        if temp < min_temp:
            min_temp = temp
    print("Min temp in July was", min_temp, "degrees!")
    

if __name__ == '__main__':
    main()