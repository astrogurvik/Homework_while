# Задача 2.43
a = int(input('Enter number a:'))
b = int(input('Enter number b:'))

print((a % b) * (b % a) + 1)

# Задача 4.137
seq_of_numbers = 1011121314151617181920212223242526272829
k = int(input('Enter a number from 1 to 40:'))
if k <= 40:
    print((seq_of_numbers // (1 * 10 ** (40 - k))) % 10)
else:
    print('error')


# Задача 5.62
def grade_average(a, b):
    test1 = type(a) is list
    test2 = type(b) is list
    if test1 is True and test2 is True:
        class_1_aver = sum(a) / len(a)
        class_2_aver = sum(b) / len(b)
        result = (class_1_aver, class_2_aver)
    else:
        result = False
        return result

    return result


class_1 = [3, 5, 4, 3, 5, 4]
class_2 = [4, 5, 4, 5, 5, 4]
classes_grade_average = grade_average(class_1, class_2)

if classes_grade_average is False:
    print('error')
else:
    print(f'Average grade of class 1 is {classes_grade_average[0]}')
    print(f'Average grade of class 2 is {classes_grade_average[1]}')


# Задача 6.97
teamList = [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
N = 11
print(teamList.index(11) + 1)


# Задача 17.7
Number = input('Enter a number:')
dig0 = ''
dig1 = ''
dig2 = ''
dig3 = ''
dig4 = ''
dig5 = ''
dig6 = ''
dig7 = ''
dig8 = ''
dig9 = ''
for i in Number:
    if int(i) == 0:
        dig0 += i
    elif int(i) == 1:
        dig1 += i
    elif int(i) == 2:
        dig2 += i
    elif int(i) == 3:
        dig3 += i
    elif int(i) == 4:
        dig4 += i
    elif int(i) == 5:
        dig5 += i
    elif int(i) == 6:
        dig6 += i
    elif int(i) == 7:
        dig7 += i
    elif int(i) == 8:
        dig8 += i
    elif int(i) == 9:
        dig9 += i
descNumber = dig9 + dig8 + dig7 + dig6 + dig5 + dig4 + dig3 + dig2 + dig1 + dig0
ascNumber = dig1 + dig2 + dig3 + dig4 + dig5 + dig6 + dig7 + dig8 + dig9
print(int(descNumber))
print(int(ascNumber))
# Задача 11.173
someStr = input()
List = list(someStr)

a_end = List.pop(-1)
List.insert(0, a_end)

print(list(someStr))
print(List)
