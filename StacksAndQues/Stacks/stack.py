#Stack looks like the below. This is a list stack 

stack = [1, 2, 3, 4, 5]

print("Original Stack", stack)

#adding item to a stack. Will appear at the top of the stack
stack.append(6)
stack.append(7)
print("Append Stack", stack)

#Pop - removes the top element in a stack
stack.pop()
print("Pop Stack", stack)


#Peek - Returns the too element in a stack 
topElement = stack[-1]
print("Stack", topElement)

#isEmpty - used to check if a stack is empty 
isEmpty = not bool(stack) 
print("isEmpty", isEmpty)

#len. To check the lenght of stack
print("Size", len(stack))

