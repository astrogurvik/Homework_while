class User:
    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_login(self, login):
        if len(login) >= 5:
            self.__login = login
        else:
            print(f'invalid login of {self.__name}')

    def get_login(self):
        return self.__login

    def set_password(self, password):
        pass_letters = ''
        for i in password:
            if i.isalpha():
                pass_letters += i
        if len(password) >= 8 and len(pass_letters) >= 3:
            self.__password = password
        else:
            print(f'invalid password of {self.__name}')

    def get_password(self):
        return self.__password


    def __str__(self):
        return (f'Имя: {self.__name}, Логин: {self.__login}, Пароль: {self.__password}')


User1 = User('Петр Иванов', 'ivanko', '123pub456')
# print(User1)
User1.set_name('Иван Сидоров')
User1.set_login('sidor')
User1.set_password('456pub123')

# print(User1)
print(User1.get_name())
print(User1.get_login())
print(User1.get_password())



