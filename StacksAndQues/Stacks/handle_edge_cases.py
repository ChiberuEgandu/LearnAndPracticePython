
class Stack:
    def __init__(self, size):
        ''' Constructor
        Parameters:
           self -- the current object
           size -- the initialize size of our stack
        '''
        self.data = list()
        self.size = size


    def isEmpty(self):
        if len(self.data) < 0:
            print()

    def push(self, item):
        ''' push -- adds something to the top of the stack
        Parameters:
           self -- the current object
           item -- the item to add to the stack
        Returns nothing
        '''
        if len(self.data) <= self.size:
            self.data.append(item)
        else:
            print("The stack is full")

    def pop(self):
        ''' pop -- removes something from the top of the stack
        Parameters:
           self -- the current object
        Returns the top element after removing it from the stack
        '''
        if len(self.data) <= 0:
            return f"The Stack is empty"
        else:
            return self.data.pop()

    def dump(self):
        ''' dump -- debugging method for the stack
        Parameters:
           self -- the current object
        '''
        for i in range(len(self.data) - 1, -1, -1):
            print(self.data[i])
    
    # CAN WE IMPLEMENT methods: size, peek, is_empty
    def size(self):
        return len(self.data)
    

    def peek(self):
        return self.data[-1]

    def is_empty(self):
        if len(self.data) <= 0:
            return True
        else:
            return False


def main():
    ''' 
    Driver program that uses our stack so that we can see it working
    '''
    my_stack = Stack(5)
    while True:
        cmd = input("push, pop, dump or exit? ")
        if cmd == "push":
            val = input("Data to add? ")
            my_stack.push(val)
        elif cmd == "pop":
            val = my_stack.pop()
            print("pop() returned --", val)
        elif cmd == "dump":
            my_stack.dump()
        elif cmd == "exit":
            break


if __name__ == "__main__":
    main()

