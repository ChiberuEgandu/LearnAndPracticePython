#Check if the stack is empty before and after pushing items.

def is_Empty(stacks):
    
    if len(stacks) <= 0:
        print("The Stack is empty")
    else:
        print("The Stack is Not Empty")




def main():
    stack = []

    stack.append(1)
    stack.append(2)
    stack.append(3)

    print("Original Stack:", stack)

    stack.pop()
    stack.pop()
    print("Poped Stack", stack)

    ##Check if stack is empty
    is_Empty(stack)

    #pop the last item
    stack.pop()
    print("Stack All Items popped:", stack)

    is_Empty(stack)





if __name__ == '__main__':
    main()

