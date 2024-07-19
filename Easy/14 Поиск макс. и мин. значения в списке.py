a = []
while True:
    a.append(int(input('Введите число, 0 чтобы закончить: ')))
    if a[len(a)-1] == 0:
        a.pop()
        break
print(f'Макс: {max(a)}\nМин: {min(a)}')