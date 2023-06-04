# Задача 9.38a
word = input('Enter a word with 12 letters:\n')
length = len(word)
third_1 = word[0:4]
third_2 = word[4:8]
third_3 = word[8:12]

if length == 12:
    print(third_2 + third_3 + third_1)
else:
    print('Error! Number of letters in your word not equal to 12.')

# Задача 9.90
# 1 способ
String = input('Enter a sentence:\n')
length = len(String)
cnt = 0
while cnt < length:
    if String[cnt] == 'е':
        print('и', end='')
    elif String[cnt] == 'e':
        print('u', end='')
    else:
        print(String[cnt], end='')
    cnt += 1

# 2 способ
String = input('\nEnter a sentence:\n')
length = len(String)
cnt = 0
result = ''
while cnt < length:
    if String[cnt] == 'е':
        result += f'и'
    elif String[cnt] == 'e':
        result += f'u'
    else:
        result += f'{String[cnt]}'
    cnt += 1
print(result)

# Задача 9.92
String = input('Enter a sentence:\n')
length = len(String)
cnt = 0
while cnt < length:
    if cnt % 2 == 0:
        print('ы', end='')
    else:
        print(String[cnt], end='')
    cnt += 1

# Задача 9.105
word = input('Enter a word with 12 letters:\n')
length = len(word)
part_1 = word[0:2]
part_2 = word[8:1:-1]
part_3 = word[9:12]

if length == 12:
    print(part_1)
    print(part_2)
    print(part_3)
    print(part_1 + part_2 + part_3)
else:
    print('Error! Number of letters in your word not equal to 12.')

# Задача 9.153
String = input('Enter a sentence:\n')
length = len(String)
cnt = 1
symbolNumber = 1
symbolNumber_max = 1
while cnt < length:
    if String[cnt] == String[cnt-1]:
        symbolNumber += 1
        if symbolNumber > symbolNumber_max:
            symbolNumber_max = symbolNumber
    else:
        symbolNumber = 1
    cnt += 1
print('The number of the same symbols is', symbolNumber_max )
