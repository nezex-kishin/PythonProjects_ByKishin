from tkinter import *
from tkinter import messagebox
import os


root = Tk()
root.geometry('600x400')
root.title('Блокнот')
root.resizable(width=False,height=False)
root.config(bg = '#F0E68C')
file_index = ''

#Окно с созданием файла
def create_file():
    def close_newwindow():
        a = messagebox.askyesnocancel(title = 'Выход',message = 'Хотите сохранить файл?')
        global file, text_field, name
        if a == True:
            file = open(f'{name}.txt','w',encoding='UTF-8')
            file.write(text_field.get('1.0',END))
            file.close()
            newwindow.destroy()
        elif a == False:
            newwindow.destroy()
    def create():
        global file, text_field, name
        while True:
            name = file_name_entry.get()
            if name == '':
                messagebox.showerror(title = 'Ошибка!',message='Поле пустое')
                break
            else:
                if os.path.exists(f'{name}') == True:
                    messagebox.showerror(title = 'Ошибка!',message='Такой файл уже существует, выберите другое название')
                    break
                else:
                    file = open(f'{name}.txt','a+',encoding='UTF-8')
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
    file_name_entry = Entry(newwindow,font = ('Georgia',13))
    file_name_entry.place(y = 240, x = 300)
    createbutton = Button(newwindow,
                          text = 'Создать',
                          font = ('Georgia',13),
                          command=create,
                          bg = '#8B4513',
                          fg = '#F0E68C')
    createbutton.pack(anchor = CENTER,expand = True)

#Окно с открытым файлом
def open_file():
    def open_selected():
        global file_index,txts
        selected_file = files_listbox.curselection()
        for i in selected_file:
            file_index = txt_files[i]
            txt = open(f'{file_index}','r',encoding='UTF-8')
            open_button.destroy()
            files_listbox.destroy()
            f_text = Frame(opened_file)
            f_text.pack(fill=BOTH, expand=1)
            txts = Text(f_text,
                              fg='black',
                              wrap=WORD,
                              spacing3=10,
                              width=30,
                              font=('Georgia', 14)
                              )
            txts.pack(expand=1, fill=BOTH, side=LEFT)
            text = txt.read()
            txts.insert('1.0',f'{text}')
    def close_openfile():
        global txts
        a = messagebox.askyesnocancel(title='Выход', message='Хотите сохранить файл?')
        if a == True:
            file = open(f'{file_index}', 'w+', encoding='UTF-8')
            file.write(txts.get('1.0',END))
            file.close()
            opened_file.destroy()
        elif a == False:
            opened_file.destroy()

    opened_file = Toplevel(root)
    opened_file.protocol('WM_DELETE_WINDOW', close_openfile)
    opened_file.title('Блокнот')
    opened_file.geometry('800x600')
    opened_file.config(bg='#F0E68C')
    opened_file.resizable(width=FALSE, height=FALSE)
    txt_files = []
    path = 'C:/Python/100PythonProjects/Normal/'
    allfiles = os.listdir(path)
    for i in range(len(allfiles)):
        if allfiles[i].endswith('.txt'):
            txt_files.append(allfiles[i])

    files_listbox = Listbox(opened_file,
                            font=('Georgia', 13), )
    for i in range(len(txt_files)):
        files_listbox.insert(i, txt_files[i])
    files_listbox.pack()
    open_button = Button(opened_file,
                         text='Открыть файл',
                         font=('Georgia', 13),
                         bg='#8B4513',
                         fg='#F0E68C',
                         command=open_selected)
    open_button.pack()

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
                  fg = '#8B4513',
                  command=open_file)
open_txt.place(x = 195,y = 250)

root.mainloop()