from classes.Methods import Methods
from classes.Stroka import Stroka
from classes.Spisok import Spisok

def length(some_object):
    return some_object.length()

def include(some_object):
    return some_object.include(sub_string)


method = Methods()
stroka = Stroka('Hello!')
Some_list = ['Hello!', 'world']
spisok = Spisok(Some_list)
sub_string = 'world'

print(length(method))
print(length(stroka))
print(length(spisok))
print()
print(include(method))
print(include(stroka))
print(include(spisok))
print()

old = 'll'
new = '!!'
print(stroka.replacing(old, new))
print()

new_item = 'The END!'
spisok.adding(new_item)
print(Some_list)



