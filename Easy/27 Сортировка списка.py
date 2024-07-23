a = []
i = 0
print('Чтобы закончить ввод, введите ноль')
while True:
    a.append(int(input('Введите число в список: ')))
    if a[i] == 0:
        a.pop(i)
        break
    i += 1
print(a)
print(sorted(a))