# Ввод списка чисел:
# someList = [int(i) for i in input('Enter a list: ').split()]
# print(someList)

# Задача: убрать из данного предложения все повторяющиеся слова.

some_string = input('Enter a sentence: ')
some_list = some_string.split()
for i in some_list:
    if some_list.count(i) > 1:
        some_list.remove(i)

result_string = ' '.join(some_list)
print(result_string)


import os

while True:
    print("0 - Выход")
    print("1 - Добавить информацию в расписание занятий")
    print("2 - Вывести информацию о расписании занятий")

    option = input("Введите номер пункта меню: ")
    if option == "0":
        break

    elif option == "1":
        infa_input = input('Добавьте информацию в расписание занятий:\n')
        with open('D://pythonProject//lessons.txt', 'a') as file:
            file.write('\n' + infa_input)

    elif option == "2":
        with open('D://pythonProject//lessons.txt', 'r') as file:
            someList = file.readlines()
            list_lessons = [lesson.rstrip("\n") for lesson in someList]
        for i in list_lessons:
            print(i)

    else:
        print('Такого пункта нет в меню')

    os.system("pause")
    os.system("cls")

print("До свидания!")


