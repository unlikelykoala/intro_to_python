# Problem 7
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

list = info.split(':')
new_info = '+'.join(list)
print(f'With split and join: {new_info}')

new2 = info.replace(':', '+')
print(f'With replace: {new2}')
