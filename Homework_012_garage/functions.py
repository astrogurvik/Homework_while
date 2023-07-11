def print_menu():
    print('0 - Выход из программы')
    print('1 - Добавить авто в гараж')
    print('2 - Удалить авто из гаража')
    print('3 - Посмотреть список авто в гараже')
    print('4 - Посчитать количество свободных мест в гараже')
    print('5 - Найти номер места авто в гараже')
    print('6 - Посчитать количество авто в гараже')


def add_car(garage):
    if garage.count('') == 0:
        print('Нет мест в гараже')
    else:
        car_number = input('Введите номер авто: ')
        print('Список мест в гараже:', garage)
        index = int(input('Введите номер места в гараже: '))
        if index < len(garage):
            garage[index] = car_number
        else:
            print('Нет такого номера места в гараже')


def remove_car(garage):
    car_number = input('Введите номер авто: ')
    if car_number in garage:
        garage[garage.index(car_number)] = ''
        print('Одно место в гараже освободилось')
    else:
        print('Авто с таким номером не найдена')


def find_car_place(garage):
    car_number = input('Введите номер авто: ')
    for i in range(len(garage)):
        if car_number in garage[i]:
            print('Номер места этого авто:', i)