#Написать функцию для определения, является ли введённое число палиндромом.

def checkPalindrom(number):
    if number[::-1] == number:
        return True

    return False

inputNumber = input('Enter a number:\n')
result = checkPalindrom(inputNumber)
print(result)


# Написать функцию, которая находит самую длинную подстроку, которая является префиксом среди массива строк. (Есть массив строк.  Например, "Потолок" и "Полёт". В данном случае, общая строка, с которой начинается каждая строка - "По". Т.е. это - самая максимальная подстрока, с которой начинается каждая строка массива).

# 1 способ
def maxSubstring(someList):
    minWord = someList[0]
    startStringLetter = ''
    for i in someList:
        if len(i) < len(minWord):
            minWord = i
    cnt = 0
    Stop = 0
    result = ''
    while cnt < len(minWord):
        for i in List:
            if minWord[cnt] != i[cnt]:
                Stop = 1
                break
            else:
                startStringLetter = minWord[cnt]
        if Stop == 1:
            break
        result += startStringLetter
        cnt += 1
    return result
List = ['morning', 'morgen', 'mar', 'mokgoon']
maxSubstring_inList = maxSubstring(List)

print('The longest substring is',maxSubstring_inList)


# 2 способ
def maxSubstring1(someList):
    minWord = someList[0]
    for i in someList:
        if len(i) < len(minWord):
            minWord = i
    cnt = 0
    result = ''

    while cnt < len(minWord):
        nLetter = ''.join([i[cnt] for i in List])
        if minWord[cnt] * len(List) != nLetter:
            break
        else:
            result += minWord[cnt]
        cnt += 1
    return result
List = ['morning', 'morgen', 'mor', 'mokgoon']
maxSubstring_inList = maxSubstring1(List)

print('The longest substring is',maxSubstring_inList)


# Написать функцию, которая определяет, правильно ли в строке расставлены скобки.
def true_brackets(sometext):
    brackets = ''
    for i in sometext:
        if i == '(':
            brackets += i
        elif i == ')':
            brackets += i
        else:
            brackets += ''

    while '()' in brackets:
        brackets = brackets.replace('()', '')

    if brackets == '':
        test = True
    else:
        test = False
    return test


text = 'Сколько (лет), (())(сколько) зим'
result = true_brackets(text)
print(result)

