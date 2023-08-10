while True:
    try:
        values_number = int(input('Введите количество элементов списка: '))
        if int(values_number) == values_number:
            break
    except ValueError:
        print('Вы ввели не число. Попробуйте снова: ')

# some_list = []
# cnt = 1
# for i in range(values_number):
#     try:
#         some_list.append(int(input(f'Введите {cnt}-е число списка из {values_number} элементов: ')))
#         cnt += 1
#         print(i)
#     except ValueError:
#         print('Вы ввели не число. Результат будет неверным.')
#         break

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

print(values_number)
print(some_list)


