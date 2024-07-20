# Problem 4
pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

print(pets['Dog'])

non_key = 'Lizard'

print(pets.get(non_key, None))

print(pets.get(non_key, '<silence'))
