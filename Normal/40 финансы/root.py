import configparser
from tkinter import *
config = configparser.ConfigParser()


root = Tk()
root.geometry('700x400')
root.resizable(height=False,width=False)
root.title('Управление финансами')

config.read('config.ini')
All_money = Label(root, text = f'Ваш счёт: \n {config.get('Value', 'money')}',font = ('Georgia',14))
All_money.place(x = 200,y = 100)

money_rewriter = Entry(root,font = ('Georgia',14))
money_rewriter.place(x = 130,y = 200)
file = open('operations.txt','a+',encoding='UTF-8')


def adder():
    amount = int(money_rewriter.get()) + config.getint('Value', 'money')
    config.set('Value','money',f'{amount}')
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    config.read('config.ini')
    All_money.config(text = f'Ваш счёт: \n {config.get('Value', 'money')}')
    operations.insert(0,f'Внесено {money_rewriter.get()}')
def minus():
    amount = config.getint('Value', 'money') - int(money_rewriter.get())
    config.set('Value', 'money', f'{amount}')
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    config.read('config.ini')
    All_money.config(text=f'Ваш счёт: \n {config.get('Value', 'money')}')
    operations.insert(0,f'Вычтено {money_rewriter.get()}')
def set_money():
    amount = int(money_rewriter.get())
    config.set('Value', 'money', f'{amount}')
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    config.read('config.ini')
    All_money.config(text=f'Ваш счёт: \n {config.get('Value', 'money')}')
    operations.insert(0, f'Задан счёт {money_rewriter.get()}')

button_add = Button(root,text = 'Добавить',font = ('Georgia',14),command=adder)
button_minus = Button(root,text = 'Вычесть',font = ('Georgia',14),command=minus)
button_set = Button(root,text = 'Задать счёт', font = ('Georgia',14),command=set_money)
button_add.place(x = 150,y = 230)
button_minus.place(x = 260,y = 230)
button_set.place(x = 190,y = 270)

operations = Listbox(root,font = ('Georgia',14))
operations.place(x = 400, y = 100)

root.mainloop()