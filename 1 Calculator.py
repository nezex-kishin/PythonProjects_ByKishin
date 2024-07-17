try:
    while True:
        print('Чтобы выйти введите 0')
        a = int(input('Введите первое число: '))
        if a == 0:
            break
        operation = input('Введите знак операции: ')
        b = int(input('Введите второе число: '))
        if operation == '+':
            print(f'Ответ: {a+b}\n')
        elif operation == '-':
            print(f'Ответ: {a-b}\n')
        elif operation == '*':
            print(f'Ответ: {a*b}\n')
        elif operation == '/':
            print(f'Ответ: {a/b}\n')
except ZeroDivisionError:
    print('Делить на ноль нельзя!')
finally:
    print('Закрываю калькулятор')
