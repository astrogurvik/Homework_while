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
