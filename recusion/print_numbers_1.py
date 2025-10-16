"""
def countdown(n):
    # base case here
    # recursive case here
Output for countdown(5):
5
4
3
2
1
Hint:

Base case: stop when n == 0

Recursive step: call countdown(n - 1)

"""

def count_down(n):
    
    #base case ---> stops the recursive case or when n == 0
    if n == 0:
        return 
    else:
        #recursive case that calls the function over and over until n == base case 
        print(n)
        return count_down(n - 1) 

"""     
Once count_down(0) returns 1, the others also return one by one — but they do not 
print anymore because all printing already happened before the recursive call.
"""
    


def count_up(n): 
    if n == 0: #base case 
        return 
    else:
        count_up(n - 1)  #check the recusive case until the base case is hit
        print(n)
    
    

def main():

    count_down(5)

    print("\n")

    count_up(5)

if __name__ == '__main__':
    main()