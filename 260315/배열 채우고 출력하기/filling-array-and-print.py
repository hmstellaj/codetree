characters = input().split()

reverse_characters = characters[::-1]
for char in reverse_characters:
    print(char, end='')