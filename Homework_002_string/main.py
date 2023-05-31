# Задача 9.14
word = input('Enter a word:\n')
lastCharacter = word[-1]
print(lastCharacter)

# Задача 9.15
word = input('Enter a word:\n')
k = int(input('Enter the number of the letter in this word you want to print:'))
length = len(word)
if (k-1) < length:
    print(word[k - 1])
else:
    print('Error! Your number of the letter is greater than the length of the word.')

# Задача 9.16
word = input('Enter a word with 4 or more letters:\n')
length = len(word)
if length >= 4:
    if word[1] == word[3]:
        print('The 2nd and 4th letters of your word are the same')
    else:
        print('The 2nd and 4th letters of your word are not the same')
else:
    print('Error! Your number of the letter is less than 4.')

# Задача 9.24
word = 'яблоко'
print(word[1] + word[2] + word[3] + word[4])
print(word[3] + word[4] + word[5])

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

# Задача 9.41
word = input('Enter football club name:')
cnt = 0
length = len(word)
while cnt < length:
    print(word[cnt])
    cnt += 1

# Задача 9.59
words = input('Enter a sentence:')
cnt = 0
number_o = 0
length = len(words)
while cnt < length:
    if words[cnt] == 'o' or words[cnt] == 'O' \
            or words[cnt] == 'о' or words[cnt] == 'О':
        number_o += 1
    cnt += 1
print('The number of letters "o" is', number_o)

# Задача 9.76(б)
words = input('Enter a sentence:')
cnt = 0
index_Last_e = 0
length = len(words)
while cnt < length:
    if words[cnt] == 'e' or words[cnt] == 'е':
        index_Last_e = cnt
    cnt += 1
print(index_Last_e)

# Вывести строку наоборот, первый способ
words = input('Enter a sentence:')
print(words[::-1])

# Вывести строку наоборот, второй способ
words = input('Enter a sentence:')
cnt = 0
length = len(words)
while cnt < length:
    print(words[-(cnt + 1)], end='')
    cnt += 1