currencies = {
    1: 'Доллар',
    2: 'Рубли',
    3: 'Евро',
    4: 'Выйти'
}

try:
    while True:
        for i in currencies:
            print(i,currencies[i])
        fc = int(input('Введите из какой валюты вы хотите перевести: '))
        if fc == 4:
            break
        oc = int(input('Введите в какую валюту вы хотите перевести: '))
        a = float(input('Введите кол-во денег: '))
        if fc == 1 and oc == 2:
            print(f'Итог: {round(a*88.5,1)} \n')
        elif fc == 2 and oc == 1:
            print(f'Итог: {round(a/88.5,1)} \n')
        elif fc == 1 and oc == 3:
            print(f'Итог: {round(a*0.91,1)} \n')
        elif fc == 3 and oc == 1:
            print(f'Итог: {round(a*1.09,1)} \n')
        elif fc == 2 and oc == 3:
            print(f'Итог: {round(a/96.79,1)} \n')
        elif fc == 3 and oc == 2:
            print(f'Итог: {round(a/0.01,1)} \n')
finally:
    pass