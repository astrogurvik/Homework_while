# Задача 6.4
cnt = 0
while True:
    n = float(input('Input number:'))

    if n > 100:
        break
    if n > 0:
        continue
    if n < 0:
        cnt += 1

print('Amount of negative numbers in your sequence is', cnt)

# Задача 6.6(б)
cnt_seq = 1
a = -4
print('The sequence is:')
while cnt_seq <= 15:
    a += 5
    cnt_seq += 1
    print(a, end=" ")
print('\n')

n = float(input('Enter number n:'))

a = 1
cnt_test = 1
while True:
    if cnt_test > 15:
        break
    if n == a:
        n = input('Error! Your number n equal to one of the numbers '
                  'of the sequence. Try again.')
    cnt_test += 1
    a += 5

step_cnt = 1
cnt_left = 0
cnt_right = 0
digit_left = 0
digit_right = 0
while step_cnt <= 15:
    step_cnt += 1
    a += 5
    diff = n - a
    if diff > 0:
        continue
    else:
        cnt_left = step_cnt - 1
        cnt_right = step_cnt
        digit_left = a - 5
        digit_right = a
        print('The number n is between', cnt_left, 'and', cnt_right,
              'ordinal numbers of the sequence, which values are',
               digit_left, 'and', digit_right, 'respectively')
        print('Difference of this values is', digit_right - digit_left)
        break

# Задача 6.42а
number1 = int(input('Input natural number:'))
number2 = number1
maxDigit1 = 0
cntMax1 = 0
number_lengs = 0
while number1 > 0:
    digit = number1 % 10
    number_lengs += 1
    if digit > maxDigit1:
        maxDigit1 = digit
        cntMax1 = number_lengs
    number1 = number1 // 10

maxDigit2 = 0
cntMax2 = 0
number_lengs = 0
while number2 > 0:
    digit = number2 % 10
    number_lengs += 1
    if maxDigit2 < digit < maxDigit1:
        maxDigit2 = digit
        cntMax2 = number_lengs
    number2 = number2 // 10

print('Number of digits in the number =', number_lengs)
print('The ordinal number of the largest digit of the number from it\'s begining is:',
      (number_lengs - cntMax1) + 1)
print('The  ordinal number of the largest digit of the number from it\'s end is:', cntMax1)
print('Largest digit of the number is:', maxDigit1)
print('The ordinal number of the second largest digit of the number from it\'s begining is:',
      (number_lengs - cntMax2) + 1)
print('The  ordinal number of the second largest digit of the number from it\'s end is:', cntMax2)
print('Second largest digit of the number is:', maxDigit2)

