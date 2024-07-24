from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import os


root = Tk()
root.geometry('600x400')
root.title('Блокнот')
root.resizable(width=False,height=False)
root.config(bg = '#F0E68C')

def create_file():
    def close_newwindow():
        global file, text_field
        if messagebox.askyesnocancel(title = 'Выход',message = 'Хотите сохранить файл?') == True:
            file.write = (f'{text_field.get("1.0",END)}')
            file.close()
            newwindow.destroy()
        elif messagebox.askyesnocancel(title = 'Выход',message = 'Хотите сохранить файл?') == False:
            file.close()
            newwindow.destroy()
        else:
            pass
    def create():
        global file, text_field
        while True:
            if file_name_entry.get() == '':
                messagebox.showerror(title = 'Ошибка!',message='Поле пустое')
                break
            else:
                if os.path.exists(f'{file_name_entry.get()}') == True:
                    messagebox.showerror(title = 'Ошибка!',message='Такой файл уже существует, выберите другое название')
                    break
                else:
                    file = open(f'{file_name_entry.get()}','w+',encoding='UTF-8')
                    createbutton.destroy()
                    file_name_entry.destroy()
                    f_text = Frame(newwindow)
                    f_text.pack(fill=BOTH,expand = 1)
                    text_field = Text(f_text,
                                      fg = 'black',
                                      wrap = WORD,
                                      spacing3=10,
                                      width = 30,
                                      font = ('Georgia',14)
                                      )
                    text_field.pack(expand = 1,fill = BOTH,side = LEFT)
                    break
    newwindow = Toplevel(root)
    newwindow.title('Блокнот')
    newwindow.geometry('800x600')
    newwindow.config(bg = '#F0E68C')
    newwindow.resizable(width=FALSE, height=FALSE)
    newwindow.protocol('WM_DELETE_WINDOW',close_newwindow)
    file_name_entry = Entry(newwindow)
    file_name_entry.pack(anchor = CENTER,expand = True)
    createbutton = Button(newwindow,text = 'Создать', command=create)
    createbutton.pack()



choose_option = Label(root,
                      text = 'Выберите опцию',
                      font=('Georgia', 30),
                      bg = '#F0E68C',
                      fg = '#8B4513')
choose_option.place(x = 140,y = 100)

create_txt = Button(root,
                    text = 'Создать файл',
                    font=('Georgia', 20),
                    bg = '#F0E68C',
                    fg = '#8B4513',
                    command=create_file)
create_txt.place(x = 200,y = 175)
open_txt = Button(root,
                  text = 'Открыть файл',
                  font=('Georgia', 20),
                  bg = '#F0E68C',
                  fg = '#8B4513')
open_txt.place(x = 195,y = 250)




root.mainloop()