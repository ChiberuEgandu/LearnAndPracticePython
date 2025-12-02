#Create a stack and remove (pop) one element from it.
#Print what you removed.
#Print the stack afterward

my_stack = []

my_stack.append(1)
my_stack.append(2)
my_stack.append(3)
my_stack.append(4)

print("Stack: ", my_stack)

#top item in stack
print(my_stack[-1])

#poping the top item in the stack
my_stack.pop()

print("Stack Poped:", my_stack)

