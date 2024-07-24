# Problem 6

my_list = [
    1, 3, 6, 11,
    4, 2, 4, 9,
    17, 16, 0,
]

new = []

for num in my_list:
    if num % 2 == 0:
        new.append('even')
        continue
    new.append('odd')

print(new)
