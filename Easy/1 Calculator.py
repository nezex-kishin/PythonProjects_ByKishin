try:
    while True:
        print('Чтобы выйти введите 0')
        a = float(input('Введите первое число: '))
        if a == 0:
            break
        operation = input('Введите знак операции: ')
        b = float(input('Введите второе число: '))
        if operation == '+':
            print(f'Ответ: {round(a+b, 2)}\n')
        elif operation == '-':
            print(f'Ответ: {round(a-b, 2)}\n')
        elif operation == '*':
            print(f'Ответ: {round(a*b, 2)}\n')
        elif operation == '/':
            print(f'Ответ: {round(a/b, 2)}\n')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
finally:
    print('Закрываю калькулятор')
