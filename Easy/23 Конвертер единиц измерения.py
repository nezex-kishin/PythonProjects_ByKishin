znach = {
    1: 'Сантиметры',
    2: 'Метры',
    3: 'Километры',
    4: 'Выйти'
}

while True:
    for i in znach:
        print(i,znach[i])
    first = int(input('Введите номер единицы измерения из которой хотите перевести: '))
    second = int(input('В какую перевести?: '))
    a = float(input('Введите значение: '))
    if first == 1 and second == 2:
        print(round(a/100,1))
    elif first == 1 and second == 3:
        print(round(a/100000,1))
    elif first == 2 and second == 1:
        print(round(a*100,1))
    elif first == 2 and second == 3:
        print(round(a/1000,1))
    elif first == 3 and second == 1:
        print(round(a*100000,1))
    elif first ==3 and second == 2:
        print(round(a*1000,1))
    else:
        break
