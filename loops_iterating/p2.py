# Problem 2
"""
Modify the age.py program you wrote in Exercise 3 of the Input/Output chapter. 
The updated code should use a for loop to display the future ages.
"""

age = int(input('How old are you? '))
decades = range(10, 41, 10)

print(type(decades))

print(f'You are {age} years old.')
for decade in decades:
    print(f'In {decade} years, you will be {decade + age} years old.')
