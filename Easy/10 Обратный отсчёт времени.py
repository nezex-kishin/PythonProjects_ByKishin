import time

while True:
    a = int(input('Введите необход. время отсчёта: '))
    while a > 0:
        print(a)
        a -= 1
        time.sleep(1)
