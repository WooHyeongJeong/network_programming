char = input('word : ')
index = char.find('a')

print(char[:index + 1])
print(char[index + 1:])