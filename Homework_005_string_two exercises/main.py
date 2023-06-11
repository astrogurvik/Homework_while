# Даны две строки. Эти строки отличаются друг от друга только одним символом.
# Т.е. вторая строка получена добавлением случайного символа в случайную
# позицию первой строки. Найти этот символ, вывести его и его индекс в строке.

someString_1 = input()
someString_2 = input()

length = len(someString_1)
cnt = 0
if len(someString_2) - len(someString_1) == 1:
    while cnt < length:
        if someString_1[cnt] != someString_2[cnt]:
            break
        cnt += 1
    print('Added symbol is', someString_2[cnt])
    print('The index of the added symbol is', cnt)
else:
    print('Strings do not satisfy the condition of the task')

# Дана строка из набора цифр, и дано число от 0 до 18 включительно.
# Надо определить, присутствуют ли в строке такие 2 цифры, сумма которых
# равна введённому числу. Если есть, то вывести эти две цифры и их индексы.
someStr = input()
someNum = int(input())

length = len(someStr)
cnt = 0
cnt1 = 0
result = False
while cnt < length:
    newStr = someStr[0:cnt] + someStr[cnt + 1:length]
    # someStr_n = someStr[cnt]
    while cnt1 < length - 1:
        # newStr_n = newStr[cnt1]
        if int(someStr[cnt]) + int(newStr[cnt1]) == someNum:
            print(f'The digits are {someStr[cnt]} and {newStr[cnt1]}')
            print(f'The indexes of this digits are {cnt} and {cnt1 + 1}')
            result = True
            break
        else:
            cnt1 += 1
    if result:
        break
    cnt1 = 0
    cnt += 1
if not result:
    print('There are no such digits')
