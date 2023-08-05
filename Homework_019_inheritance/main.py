class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color

class Cat(Animal):
    def __init__(self, name, color, voice):
        super().__init__(name, color)
        self.voice = voice

    def print_voice(self):
        print(self.voice)

    def set_name(self, new_name):
        if new_name != '':
            self.name = new_name

    def get_name(self):
        return self.name

    def set_color(self, new_color):
        if new_color != '':
            self.color = new_color

    def get_color(self):
        return self.color

    def __str__(self):
        return (f'Здравствуйте! Я - {self.color} кот {self.name}. {self.voice}')

class Dog(Animal):
    def __init__(self, name, color, voice):
        super().__init__(name, color)
        self.voice = voice

    def print_voice(self):
        print(self.voice)

    def set_name(self, new_name):
        if new_name != '':
            self.name = new_name

    def get_name(self):
        return self.name

    def set_color(self, new_color):
        if new_color != '':
            self.color = new_color

    def get_color(self):
        return self.color

    def __str__(self):
        return (f'Здравствуйте! Я - {self.color} пёс {self.name}. {self.voice}')

catName = input('Введите имя кота: ')
catColor = input('Введите цвет кота: ')
catVoice = 'Мяу!'
cat = Cat(catName, catColor, catVoice)
print()
print('Имя кота: ', cat.get_name())
print('Цвет кота: ', cat.get_color())
print()
cat.set_name('Васька')
cat.set_color('рыжий')
print(cat)
cat.print_voice()

dogName = input('Введите имя пса: ')
dogColor = input('Введите цвет пса: ')
dogVoice = 'Гав!'
dog = Dog(dogName, dogColor, dogVoice)
print()
print('Имя пса: ', dog.get_name())
print('Цвет пса: ', dog.get_color())
dog.set_name('Цезарь')
dog.set_color('Белый')
dog.print_voice()

