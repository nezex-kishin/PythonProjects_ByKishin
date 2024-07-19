import random

moves = {1: 'Камень',
     2: 'Ножницы',
     3: 'Бумага',
     4: 'Выйти из игры'
     }
while True:
    for i in moves:
        print(i,moves[i])
    move = int(input('Выберите действие: '))
    bot_move = random.randint(1,3)
    if move == bot_move:
        print(f'Робот выбрал {moves[bot_move]}, ничья!')
    elif (move == 1 and bot_move == 2) or (move == 2 and bot_move == 3) or (move == 3 and bot_move == 1):
        print(f'Робот выбрал {moves[bot_move]}, Вы победили!')
    elif move == 4:
        break
    else:
        print(f'Робот выбрал {moves[bot_move]}, Вы проиграли!')
