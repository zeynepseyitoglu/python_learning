#Mail merging challenge
PLACEHOLDER = '[name]'

#names in a list
with open('my_file.txt', 'r') as namesFile:
    names = namesFile.readlines()

with open('letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)
        with open(f'letter_for_{stripped_name}.txt', 'w') as completed_letter:
            completed_letter.write(new_letter)