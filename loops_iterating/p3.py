# Problem 3
"""
Use a while loop to print the numbers in my_list, one number per line.
Then, do the same with a for loop.
"""

my_list = [6, 3, 0, 11, 20, 4, 17]
max = len(my_list)
counter = 0

print('WHILE')
while counter < max:
    print(my_list[counter])
    counter += 1

print()

print('FOR')
for element in my_list:
    print(element)
