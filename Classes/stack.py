class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return f"The list is empty"
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return f"The list is empty"
    
    def __str__(self):
        return f"Stack: {self.items}"

def main():
    s = Stack()
    print(s)

    s.push(1)
    s.push(2)
    print(s)

    print(s.size())
    print(s.is_empty())

if __name__ == '__main__':
    main()