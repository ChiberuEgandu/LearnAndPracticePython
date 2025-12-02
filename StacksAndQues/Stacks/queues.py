queue = []

queue.append('A')
queue.append('B')
queue.append('C')

print("Queue:", queue)

#Peek - Check for front element
frontElement = queue[0]
print("Front Element", frontElement)

#Dequeue - Removes and returns first element
poppedElement = queue.pop(0)
print("Dequeue:", poppedElement)
print("Queue After Dequeue:", queue)

isEmpty = not bool(queue)
print("isEmpty:", isEmpty)