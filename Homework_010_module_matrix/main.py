# Задача 12.5 (б)
import random
import matrix_rand_1_9_output

X = int(input('Enter a number of rows:'))
Y = int(input('Enter a number of columns:'))
s = int(input("Enter the column number: "))
result_matrix = matrix_rand_1_9_output.matrix_output(X, Y)
print()

if s > Y:
    print("Error! The column number is greater than the number of matrix columns.")
else:
    for i in range(X):
        print(result_matrix[i][s - 1], end=' ')

# Задача 12.6 (б)
X = int(input('Enter a number of rows:'))
Y = int(input('Enter a number of columns:'))
m = int(input("Enter the row number: "))
result_matrix = matrix_rand_1_9_output.matrix_output(X, Y)
print()

if m > X:
    print("Error! The row number is greater than the number of matrix rows.")
else:
    print(result_matrix[m - 1])

# Задача 12.16 (a)
X = int(input('Enter a number of rows:'))
Y = int(input('Enter a number of columns:'))
result_matrix = matrix_rand_1_9_output.matrix_output(X, Y)
element1 = result_matrix[random.randint(0, X - 1)][random.randint(0, Y - 1)]
print('element1 is', element1)
element2 = result_matrix[random.randint(0, X - 1)][random.randint(0, Y - 1)]
print('element2 is', element2)
dif = element1 - element2
print('The difference is', dif)

# Задача 12.33 (a)
X = int(input('Enter a number of rows :'))
Y = int(input('Enter a number of columns greater than 4:'))
result_matrix = matrix_rand_1_9_output.matrix_output(X, Y)
print()
if Y < 5:
    print("Error! The number of columns is not greater than 4.")
else:
    for i in range(X):
        print(result_matrix[-i - 1][4], end=' ')

# Задача 12.62 (a)
X = int(input('Enter a number of rows:'))
Y = int(input('Enter a number of columns:'))

result_matrix = matrix_rand_1_9_output.matrix_output(X, Y)

for i in range(X):
    print(f'The sum of elements of the {i + 1 } row is {sum(result_matrix[i])}')

# Задача 12.90
X = int(input('Enter a number of rows:'))
Y = int(input('Enter a number of columns:'))

result_matrix = matrix_rand_1_9_output.matrix_output(X, Y)

for i in range(X):
    print(f'The max element of the {i + 1 } row is {max(result_matrix[i])}')
    print(f'The min element of the {i + 1 } row is {min(result_matrix[i])}')


