# Problem 8

my_set = {
    'Fluffy',
    'Butterscotch',
    'Pudding',
    'Cheddar',
    'Cocoa',
}

new_d = {key:len(key)
         for key in my_set
         if len(key) % 2 != 0}

print(new_d)
