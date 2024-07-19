import random
from tkinter import *
fruits = ['1','2','3']

root = Tk()
root.geometry('300x300')
root.resizable(width=False,height=False)
root.title('Игровой автомат')

label1 = Label(root,text = '',font = 'Arial 15')
label2 = Label(root,text = '',font = 'Arial 15')
label3 = Label(root,text = '',font = 'Arial 15')
label1.place(x = 100,y = 50)
label2.place(x = 150,y = 50)
label3.place(x = 200,y = 50)
winorlose = Label(root,text = '',font = 'Arial 16')
winorlose.place(x = 125,y = 200)

def Roll():
    a = random.choice(fruits)
    b = random.choice(fruits)
    c = random.choice(fruits)
    label1.config(text = f'{a}')
    label2.config(text=f'{b}')
    label3.config(text=f'{c}')
    if a == b == c:
        winorlose.config(text = 'WIN')
    else:
        winorlose.config(text = 'LOSE')

button = Button(root, text = 'Крутить', command = Roll, font = 'Arial 10')
button.place(x=125,y = 100)

root.mainloop()