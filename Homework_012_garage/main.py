# Программа учета мест в гараже
import os
import functions
Garage = [''] * 3
os.system('cls')

while True:
    functions.print_menu()

    choice = input('Введите номер пункта меню: ')

    if choice == '0':
        break
    elif choice == '1':
        functions.add_car(Garage)
    elif choice == '2':
        functions.remove_car(Garage)
    elif choice == '3':
        print('Список мест в гараже:', Garage)
    elif choice == '4':
        print('В гараже', Garage.count(''), 'свободных мест')
    elif choice == '5':
        functions.find_car_place(Garage)
    elif choice == '6':
        print('В гараже', len(Garage) - Garage.count(''), 'авто')
    else:
        print('Неправильно выбран пункт меню')

    os.system('pause')
    os.system('cls')

print('Работа программы завершена')

