# Problem 4

def increment_counter():
    global counter 
    counter += 1
    return counter

counter = 5
increment_counter()
print(counter)
