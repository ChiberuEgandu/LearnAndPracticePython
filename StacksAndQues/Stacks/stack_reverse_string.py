#Use a stack to reverse a string (e.g., "hello" → "olleh").
#Push each letter, then pop them to build the reversed word.



def main():

    stack = []

    char = 'hello'
    print("Original Char", char)

    #while loop
    i = 0
    while i < len(char):
        stack.append(char[i])
        i += 1
    
    print("My_Stack:", stack)

    #empty str/char to store reversed string

    #Create an empty string or a character array to store the reversed string.
    #  While the stack is not empty, pop a character from the stack and append 
    # it to the new string or character array. Because of LIFO, the characters 
    # will be popped in the reverse order of their original appearance in the string.

    reverse_str = []


    while len(stack) > 0:
        reverse_str.append(stack.pop())
        
    
    print("Reversed:", reverse_str)

    reversed_char = "".join(reverse_str)
    print("Original char reversed :", reversed_char)


if __name__ == '__main__':
    main()
