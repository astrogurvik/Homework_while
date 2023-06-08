# Задача 9.82
someString = input('Enter a sentence:')
cnt = 0
length = len(someString)
while True:
    if someString[cnt] == ' ':
        cnt += 1
        continue
    if someString[cnt] != ' ':
        break
subString = someString[cnt:]
# Можно вместо цикла использовать метод .strip()

if ' ' in subString:
    index1 = subString.index(' ')
    result = subString.count('o', 0, index1 )
else:
    result = subString.count('o')

print('The number of letter "o" in the first word of the sentence is',result)

# Задача 9.141
someString = input('Enter text:')
length = len(someString)
cnt = 0
summa = 0
maxDigit = 0
while cnt < length:
    if someString[cnt].isdigit():
        digit = int(someString[cnt])
        summa += digit
        if digit > maxDigit:
            maxDigit = digit
    cnt += 1
print('The sum of all digits in the text is', summa)
print('The biggest digit in the text is', maxDigit)

# Задача 9.161
# Если между словами больше одного пробела,
# то метод на строке 42 обязателен
InputString = input('Enter 3 words:')
someString = ' '.join(InputString.split())

length = len(someString)
index1 = someString.index(' ')
word_1 = someString[0:index1]

index2 = someString.index(' ', index1 + 1)
word_2 = someString[index1 + 1:index2]

word_3 = someString[index2 + 1:]

cnt = 0
result = ''
while cnt < length:
    letter =  someString[cnt]
    if letter in word_1:
        result += letter + ' '
    cnt += 1
print(result)

# Задача 9.166
# Если заморачиваться с разными символами и пробелами
# в предложении и переставлять исключительно слова
# без символов, то получается как-то так.
InputString = input('Enter a sentence:')
InputString = InputString.strip()
someString = ' '.join(InputString.split())
someString = someString.replace('!', '')
someString = someString.replace(',', '')
someString = someString.replace('.', '')
someString = someString.replace(':', '')

index1 = someString.index(' ')
first_word = someString[0:index1]

index2 = someString.rindex(' ')
last_word = someString[index2 + 1:]

result = InputString.replace(last_word, first_word)
result = result.replace(first_word, last_word, 1)
print(result)

# Если не заморачиваться с разными символами и пробелами
# в предложении, то можно решить задачу гораздо проще.
someString = input('Enter a sentence:')
index1 = someString.index(' ')
first_word = someString[0:index1]

index2 = someString.rindex(' ')
last_word = someString[index2 + 1:]

middle = someString[index1 + 1:index2]

print(last_word, middle, first_word)
# или
print('{0} {1} {2}'.format(last_word, middle, first_word))

# Задача 9.178 а) и б)
InputString = input('Enter a sentence:')
InputString = InputString.strip()
someString = ' '.join(InputString.split())
someString = someString.replace('!', '')
someString = someString.replace(',', '')
someString = someString.replace('.', '')
someString = someString.replace(':', '')

index1 = 0
while True:
    if ' ' in someString:
        index1 = someString.index(' ')
        word = someString[0:index1]
        someString = someString[index1 + 1:]
        word = (word[:-1].replace(word[-1], '') + word[-1]).replace('a', 'o', 1)
        print(word)
    else:
        word = someString
        word = (word[:-1].replace(word[-1], '') + word[-1]).replace('a', 'o', 1)
        print(word)
        break

# Задача 9.178 г
someString = input('Enter a sentence:')
length_someString = len(someString)
current_word = ''
longest_word = ''
cnt = 0
while cnt < length_someString:
    if someString[cnt].isalpha() == True:
        current_word += someString[cnt]
        cnt += 1
    elif someString[cnt] != someString.isalpha() and len(current_word) >= 0:
        if len(current_word) > len(longest_word):
            longest_word = current_word
            current_word = ''
            cnt += 1
        else:
            current_word = ''
            cnt += 1
if len(current_word) > len(longest_word):
    longest_word = current_word
print('The largest world in the sentence is', longest_word)
length_longest_word = len(longest_word)
if length_longest_word % 2 == 1:
    result = longest_word.replace(longest_word[length_longest_word // 2 ], '')
else:
    result = longest_word.replace(longest_word[length_longest_word // 2 - 1:length_longest_word // 2 + 1], '')
print(result)
