# Задача 8.54
someNumber = int(input('Enter a number: '))
cnt = 1
while cnt <= someNumber:
    if someNumber % cnt == 0:
        print(cnt, end=', ')
    cnt += 1
print()

# Задача 9.182
def only_words(somestring):
    somestring = somestring.replace('!', '')
    somestring = somestring.replace(',', '')
    somestring = somestring.replace('.', '')
    somestring = somestring.replace(':', '')
    somestring = somestring.replace('?', '')
    somestring = somestring.replace('-', '')
    result = somestring
    return result

someStr = input('Введите два предложения:\n')
List = someStr.split('.')
Str1 = only_words(List[0])
Str2 = only_words(List[1])
List1 = set((Str1.split()))
List2 = set((Str2.split()))
Result = []
for i in List1:
    if i not in List2:
        Result.append(i)

print(Result)
print()

# Задача 9.183
someStr = input('Введите два предложения:\n')
List = only_words(someStr.lower()).split()

Result = []
for i in List:
    if List.count(i) == 1:
        Result.append(i)
print(Result)
print()

# Задача 11.245
someList = [1, 0, -13, -11, 4, 6, -12, 5]
negativeList = []
positiveList = []
zeroList = []
for i in someList:
    if i < 0:
        negativeList.append(i)
    elif i == 0:
        zeroList.append(i)
    else:
        positiveList.append(i)
print(negativeList + zeroList + positiveList)
print()

# Задача. Сумма двух матриц
import random

def matrix_output(x_rows, y_columns):
    matrix = [[]] * x_rows
    for x in range(x_rows):
        matrix[x] = [0] * y_columns

    for x in range(x_rows):
        for y in range(y_columns):
            matrix[x][y] = random.randint(1, 9)

    for x in range(x_rows):
        print(matrix[x])

    return matrix


X = int(input('Enter a number of rows: '))
Y = int(input('Enter a number of columns: '))

print('Matrix_1 :')
matrix1 = matrix_output(X, Y)
print()
print('Matrix_2 :')
matrix2 = matrix_output(X, Y)

res_matrix = [[]] * X
for i in range(X):
    res_matrix[i] = [0] * Y
for i in range(X):
    for j in range(Y):
        res_matrix[i][j] = matrix1[i][j] + matrix2[i][j]

print()
print('The sum of matrix1 and matrix2:')
for i in range(X):
    print(res_matrix[i])




