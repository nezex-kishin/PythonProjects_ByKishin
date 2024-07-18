import random
from tkinter import *
variants = {
    1: 'Орёл',
    2: 'Решка'
}
root = Tk()
root.title('Коин флип')
root.geometry('300x100')
coin = Label(root, text = 'Подбросьте монету!', font = 'Arial 20')
def coin_flip():
    coin.config(text = variants[random.randint(1,2)])
flip = Button(root, text = 'Подбросить', font = 'Arial 20',command=coin_flip)
coin.pack()
flip.pack()
root.mainloop()
