def template_operation(type_operation):
    if type_operation == '+':
        return lambda _num1, _num2: f'{_num1} + {_num2} = {_num1 + _num2}'
    elif type_operation == '-':
        return lambda _num1, _num2: f'{_num1} - {_num2} = {_num1 - _num2}'
    elif type_operation == '**':
        return lambda _num1, _num2: f'{_num1} ** {_num2} = {_num1 ** _num2}'
    elif type_operation == '/':
        return lambda _num1, _num2: f'{_num1} / {_num2} = {_num1 / _num2}'
    elif type_operation == '%':
        return lambda _num1, _num2: f'{_num1} % {_num2} = {_num1 % _num2}'
    elif type_operation == '*':
        return lambda _num1, _num2: f'{_num1} * {_num2} = {_num1 * _num2}'
    else:
        return lambda _num1, _num2: f'There is no so kind of operation: {_num1} {type_operation} {_num2}'

operation = input('Enter a type of operation (+, -, *, **, / or %): ')
funct_calk = template_operation(operation)

number1 = int(input('Enter the number1: '))
number2 = int(input('Enter the number2: '))
result = funct_calk(number1, number2)
print(result)
