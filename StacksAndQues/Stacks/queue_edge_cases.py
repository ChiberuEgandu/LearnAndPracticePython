class Queue:
    def __init__(self, limit):
        ''' Constructor
        Parameters:
           self -- the current object
           limit -- the initialize size of our queue
        '''
        self.data = list()
        self.limit = limit

    def enqueue(self, item):
        ''' enqueue -- adds something to the end of the queue
        Parameters:
           self -- the current object
           item -- the item to add to the queue
        Returns nothing
        '''
        if len(self.data) <= self.limit:
            print("The queue is empty")
        else:
            self.data.append(item)

    def dequeue(self):
        ''' deqeuue -- removes something from the front of the queue
        Parameters:
           self -- the current object
        Returns the element of the front of the queue
        '''
        if len(self.data) <= 0:
            return "The queue is empty"
        else:
            return self.data.pop(0)
        
    def dump(self):
        ''' dump -- debugging method for the queue
        Parameters:
        self -- the current object
        '''
        print(self.data)

    #CAN WE IMPLEMENT ADDITIONAL METHODS: is_empty, size, peek
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
    Driver program that uses our queue so that we can see it working
    '''
    my_queue = Queue(10)
    while True:
        cmd = input("enqueue, dequeue, dump or exit (e, d, dump or exit)? ")
        if cmd == "e":
            val = input("Data to add? ")
            my_queue.enqueue(val)
        elif cmd == "d":
            val = my_queue.dequeue()
            print("dequeue() returned --", val)
        elif cmd == "dump":
            my_queue.dump()
        elif cmd == "exit":
            break
