# Задача 11.16
List = [1, -4, 3, 0, -5, 6, 4, 8, 9, 3, 1]
s = int(input())
k = int(input())
print(List)

if List[s] > 0:
    print(f'The list element at index {s} is positive number')
else:
    print(f'The list element at index {s} isn\'t positive number')

if List[k] % 2 == 0:
    print(f'The list element at index {k} is an even number')
else:
    print(f'The list element at index {k} isn\'t an even number')

if List[s] > List[k]:
    print(f'The list element at index {s} is greater than the list element at index {k}')
if List[k] > List[s]:
    print(f'The list element at index {k} is greater than the list element at index {s}')

# Задача 11.18
List = [10, 14, 23, 20, 15, 36, 44, 58, 91, 32, 2]
length = len(List)
cnt = 0
result = []
while cnt < length:
    result.append(List[cnt] - 20)
    cnt += 1
print(result)

LastIndex = List[-1]
cnt = 0
result = []
while cnt < length:
    result.append(List[cnt] * LastIndex)
    cnt += 1
print(result)

B = 5
cnt = 0
result = []
while cnt < length:
    result.append(List[cnt] + B)
    cnt += 1
print(result)

# Задача 11.21
January = [1, 2, 3, 4]
print('January snowfall is', sum(January))

# Задача 11.30
school_students = [21, 21, 21, 22]
all_students = sum(school_students)

if all_students >= 1000:
    print('The number of all students in the school is more than 999')
else:
    print('The number of all students in the school is less than 1000')

# Задача 11.36
List = [100, -14, 23, 200, 0, 15, -36, 44, 58, 91, 32, -2]
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] >= 0:
        result.append(List[cnt])
    cnt += 1
print(result)

cnt = 0
result = []
while cnt < length:
    if List[cnt] <= 100:
        result.append(List[cnt])
    cnt += 1
print(result)

# Задача 11.39
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
length = len(List)
cnt = 1
result = []
while cnt < length:
    result.append(List[cnt])
    cnt += 2
print(result)

cnt = 2
result = []
while cnt < length:
    result.append(List[cnt])
    cnt += 3
print(result)

# Задача 11.52
List = [100, -14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] % 10 == 4:
        result.append(List[cnt] // 2)
    elif List[cnt] % -10 == -4:
        result.append(List[cnt] * 2)
    else:
        result.append(List[cnt])
    cnt += 1
# если элемент списка - отрицательное число, то, чтобы его
# уменьшить вдвое, надо умножить, а не разделить на 2.
# Также % в строке 8 можно заменить на строчный метод:
# elif str(List[cnt])[-1] == '4':
print(result)

List = [100, 14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] % 2 == 0:
        result.append(List[cnt] ** 2)
    else:
        result.append(List[cnt] * 2)
    cnt += 1
print(result)

List = [100, 14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
a = 5
b = 1
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] % 2 == 0 and cnt % 2 != 0:
        result.append(List[cnt] + a)
    elif List[cnt] % 2 != 0 and cnt % 2 == 0:
        result.append(List[cnt] - b)
    elif List[cnt] % 2 == 0 and cnt % 2 == 0:
        result.append(List[cnt] + a - b)
    else:
        result.append(List[cnt])
    cnt += 1
# в этой задаче есть нюанс:
# номера и индексы элементов могут не быть одним и тем же числом
# (тогда используем cnt + 1)
print(result)

# Задача 11.53
List = [100, 14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] % 10 == 0:
        result.append(0)
    else:
        result.append(List[cnt])
    cnt += 1
print(result)

List = [100, 14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] % 2 != 0:
        result.append(List[cnt] * 2)
    else:
        result.append(List[cnt] // 2)
    cnt += 1
print(result)

List = [100, 14, 23, 200, 0, 15, 36, 44, 58, 91, 32, 2]
m = 5
n = 1
length = len(List)
cnt = 0
result = []
while cnt < length:
    if List[cnt] % 2 != 0 and cnt % 2 == 0:
        result.append(List[cnt] - m)
    elif List[cnt] % 2 != 0 and cnt % 2 != 0:
        result.append(List[cnt] - m + n)
    elif List[cnt] % 2 == 0 and cnt % 2 != 0:
        result.append(List[cnt] + n)
    else:
        result.append(List[cnt])
    cnt += 1
# в этой задаче тоже есть нюанс:
# номера и индексы элементов могут не быть одним и тем же числом
# (тогда используем cnt + 1)
print(result)

