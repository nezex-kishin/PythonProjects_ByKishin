import random
import time

randomnumber = random.randint(int(input('Введите первую границу загаданного пароля: ')),int(input('Вторая граница: ')))
while True:
    a = int(input('Попробуйте угадать: '))
    if a != randomnumber:
        print('Попробуйте ещё раз')
        time.sleep(0.5)
        continue
    else:
        break
print('Поздравляю, Вы угадали :)')