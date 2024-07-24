# Problem 4
'''
Use a while loop to print all numbers in my_list with even values, one number per line. 
Then, print the odd numbers using a ' for' loop.
'''

my_list = [6, 3, 0, 11, 20, 4, 17]
len = len(my_list)

print('Evens')
counter = 0
while counter < len:
    if my_list[counter] % 2 == 0:
        print(my_list[counter])
    counter += 1

print()

print('Odds')
for num in my_list:
    if num % 2 == 1:
        print(num)
