# Write file
with open('message.txt', 'w', encoding='utf-8') as file:
    file.write('Hello\n')
    file.write('Python\n')
    file.write('Programming')

# Read file
with open('message.txt', 'r', encoding='utf-8') as file:
    print(file.read())

# Read file with enumerate function
with open('message.txt', 'r', encoding='utf-8') as file:
    for count, text in enumerate(file, 1):
        print(count, text, end='')
