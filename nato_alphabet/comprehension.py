#List comprehension
#new_list = [new_item for item in list if something]

#Examples:
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]

name = 'Ava'
letter_list = [letter.upper() for letter in name]
print(letter_list)

new_name = ''.join(letter_list)
print(new_name)

names = ['Alex', 'Beth', 'Caroline', 'David', 'Rafael', 'Fred']
short_names = [name for name in names if len(name) < 5]

print(short_names)