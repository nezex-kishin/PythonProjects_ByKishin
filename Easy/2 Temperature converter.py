try:
    temperatures = {
        1:'Градусы Цельсия',
        2:'Градусы Фаренгейта',
        3:'Градусы Кельвина',
        4:'Выключить конвертор'
    }
    while True:
        for i in temperatures:
            print(i,temperatures[i])
        income_temperature = int(input('Введите из какой СИ вы хотите перевести: '))
        if income_temperature == 4:
            break
        outcome_temperature = int(input('Введите в какую СИ вы хотите перевести: '))
        a = float(input('Введите температуру: '))
        if income_temperature == 1 and outcome_temperature == 2:
            print(f'Итог: {round((a*(9/5))+32,1)} F\n')
        elif income_temperature == 2 and outcome_temperature == 1:
            print(f'Итог: {round((a-32)*(9/5),1)} C\n')
        elif income_temperature == 1 and outcome_temperature == 3:
            print(f'Итог: {round(a+273.15,1)} K\n')
        elif income_temperature == 3 and outcome_temperature == 1:
            print(f'Итог: {round(a-273.15,1)} C\n')
        elif income_temperature == 2 and outcome_temperature == 3:
            print(f'Итог: {round((a-32)*(9/5)+273.15,1)} K\n')
        elif income_temperature == 3 and outcome_temperature == 2:
            print(f'Итог: {round((a-273.15)*(9/5)+32,1)} F\n')

finally:
    print('Закрываю конвертер')