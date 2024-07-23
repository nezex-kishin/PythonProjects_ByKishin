def nod(first,second):
    i = 1
    a = []
    if first % second == 0:
        print('nod:',second)
    elif second % first == 0:
        print('nod:',first)
    else:
        while i < max(first,second):
            if second % i == 0 and first % i == 0:
                a.append(i)
                i += 1
            else:
                i += 1
        print('nod:',max(a))
def nok(first,second):
    i = max(first,second)
    if max(first,second) % min(first,second) == 0:
        print('nok:',max(first,second))
    else:
        while True:
            if first % i == 0 and second % i == 0:
                print('nok:',i)
                break
            else:
                i += 1

first = int(input('первое число: '))
second = int(input('второе число: '))
nod(first,second)
nok(first,second)