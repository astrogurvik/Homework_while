# Такая обработка ошибки всё равно приводит к ошибке выполнения,
# если пользователь второй раз вводит не число:
# try:
#     values_number = int(input('Введите количество элементов списка: '))
# except ValueError:
#     print('Вы ввели не число.')
#     values_number = int(input('Попробуйте снова. Введите количество элементов списка: '))

while True:
    try:
        values_number = int(input('Введите количество элементов списка: '))
        break
    except ValueError:
        print('Вы ввели не число. Попробуйте снова: ')

# Такая обработка ошибки всё равно приводит к ошибке выполнения,
# если пользователь второй раз вводит не число:
# some_list = []
# for i in range(values_number):
#     try:
#         some_list.append(int(input(f'Введите {i + 1}-е число списка из {values_number} элементов: ')))
#     except ValueError:
#         print('Ошибка! Вы должны были вести число!')
#         some_list.append(int(input(f'Введите {i + 1}-е число списка из {values_number} элементов: ')))

some_list = []
cnt = 1
while True:
    try:
        some_list.append(int(input(f'Введите {cnt}-е число списка из {values_number} элементов: ')))
        cnt += 1
        if len(some_list) >= values_number:
            break

    except ValueError:
        print('Вы ввели не число. Попробуйте снова: ')


def quicksort(alist, start, end):
    '''Sorts the list from indexes start to end - 1 inclusive.'''
    if end - start > 1:
        p = partition(alist, start, end)
        quicksort(alist, start, p)
        quicksort(alist, p + 1, end)

print(f'Ваш мписок из {values_number}: {some_list}')
def partition(alist, start, end):
    pivot = alist[start]
    i = start + 1
    j = end - 1

    while True:
        while (i <= j and alist[i] <= pivot):
            i = i + 1
        while (i <= j and alist[j] >= pivot):
            j = j - 1

        if i <= j:
            alist[i], alist[j] = alist[j], alist[i]
        else:
            alist[start], alist[j] = alist[j], alist[start]
            return j

quicksort(some_list, 0, len(some_list))
print(f'Список после сортировки: {some_list}')
