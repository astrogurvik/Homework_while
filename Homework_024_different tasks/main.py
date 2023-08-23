# Ввести строку с клавиатуры, представляющую собой текст.
# 1) Вывести количество предложений в тексте
# 2) Вывести количество слов в тексте
# 3) Вывести 3 самых больших слова
some_str = input('Enter a text: ')
some_list_sent = some_str.split('.')
some_list_sent.pop()
print(f' Количество предложений в тексте: {len(some_list_sent)}')

some_list_words = some_str.replace('.', '').split(' ')
print(f' Количество слов в тексте: {len(some_list_words)}')

some_list_words.sort(key=lambda long: len(long))

print(f'Три самых длинных слова: {some_list_words[-1]}, {some_list_words[-2]}, {some_list_words[-3]}')

# В одномерном массиве, состоящем из n вещественных элементов, вычислить:
# 1) номер минимального элемента массива
# 2) сумму элементов массива, расположенных между первым и вторым
#    отрицательными элементами
# Преобразовать массив таким образом, чтобы сначала располагались все элементы,
# модуль которых не превышает 1, а потом все остальные.

some_list = [float(i) for i in input('Enter a list: ').split()]
min_num = min(some_list)
index = some_list.index(min_num)
print(f'Индекс минимального элемента массива: {index}')
# или так:
for index, value in enumerate(some_list):
    if value == min_num:
        print(f'Индекс минимального элемента массива: {index}')

cnt_list =[]
for index, value in enumerate(some_list):
    if len(cnt_list) > 1:
        break
    if value < 0:
        cnt_list.append(index)

sum_list = sum(some_list[cnt_list[0] + 1:cnt_list[1]])
print(sum_list)

new_list_left = []
new_list_right = []
for i in some_list:
    if abs(i) < 1:
        new_list_left.append(i)
    else:
        new_list_right.append(i)
new_list_result = new_list_left + new_list_right
print(f'Преобразованный массив: {new_list_result}')
