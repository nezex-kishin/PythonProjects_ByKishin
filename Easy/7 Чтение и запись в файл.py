file = open("my_file.txt",encoding='UTF-8')
operations = {
    1: 'Записать',
    2: 'Прочитать',
    3: 'Закрыть и сохранить'
}
try:
    while True:
        for i in operations:
            print(i,operations[i])
        oper = int(input('Введите номер операции: '))
        if oper == 1:
            file = open("my_file.txt", 'a+', encoding='UTF-8')
            a = str(input('Введите строку которую хотите добавить в файл: '))
            file.write(f'{a} \n')
        elif oper == 2:
            file = open("my_file.txt",'r',encoding='UTF-8')
            print(f'\n{file.read()}')
        else:
            file.close()
            break
except:
    print('Неправильный номер операции')
finally:
    print('Закрываю программу')
