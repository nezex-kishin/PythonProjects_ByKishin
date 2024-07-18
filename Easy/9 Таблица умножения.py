while True:
    number = int(input('Введите цифру: '))
    if number > 9 or number < 1:
        print('Попробуйте снова')
        continue
    for i in range(1,11):
        print(f'{number}*{i} {number*i}')