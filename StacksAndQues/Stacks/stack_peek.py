#Implement a peek() function that returns the top element without removing it.
def peek(top_item):
    return top_item[-1]

def size(stack_size):
    return len(stack_size)


def main():

    stack = []

    stack.append(2)
    stack.append(3)
    stack.append(5)
    stack.append(8)

    print("Current Stack: ", stack)

    print("Top item:", peek(stack))
    print("Stack size:", size(stack))

    stack.pop()
    print("Current Stack: ", stack)

    print("Top item:", peek(stack))
    print("Stack size:", size(stack))




if __name__ == '__main__':
    main()

