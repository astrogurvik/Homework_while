def print_menu():
    print('1) посетители коворкинга')
    print('2) количество посетителей')
    print('3) добавить посетителя')
    print('4) удалить посетителя')
    print('0) Выход из программы')

def print_users(local_users):
    if len(local_users) == 0:
        print('Коворкинг пуст')
    index = 1
    for i in local_users:
        print(f'{index}) {i}')
        index += 1

def print_count_users(local_users):
    print(f'Количество посетителей коворкинга: {len(local_users)}')

def add_user(local_users, local_max_users):
    if len(local_users) < local_max_users:
        local_user = input('Введите нового посетителя: ')
        local_users.add(local_user)
    else:
        print('Коворкинг заполнен')

def remove_user(local_users):
    print(f'Удалите посетителя из списка: {local_users}')
    local_user = input('Введите посетителя, которого хотите удалить: ')
    if local_user in local_users:
        local_users.remove(local_user)
    else:
        print('Посетитель не найден')


