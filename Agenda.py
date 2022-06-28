from tkinter import *
import tkinter as tk 
from tkinter import filedialog
import os
from Banco_db import Banco

pastaApp = os.path.dirname(__file__)
db = Banco()
db.path = pastaApp
db.arquivo = "Banco.db"
screen_main_width  = 500
screen_main_height = 300

def main():    
    def clear():
        clear_error()
        global main_frame
        global down_frame
        try:
            main_frame.destroy()
            down_frame.destroy()
        except:
            pass
        main_frame = Frame(window, bg="#dde", borderwidth=0,relief=FLAT).place(x=0, y=0, width=screen_main_width, height=screen_main_height-20)
        down_frame = Frame(window, bg="#fff", borderwidth=1,relief=FLAT).place(x=0 ,y=screen_main_height-20, width=screen_main_width, height=20)
    
    def clear_error():
        global error_label
        try:
            error_label.destroy()
        except:
            pass
        error_label = Label(down_frame, fg="RED", bg="#fff")

    def ticket(opc):
        def save():
            lista_tabelas = db.consult(" SELECT name FROM sqlite_master ")
            codigo = entry_codigo.get()
            if codigo in lista_tabelas:
                pass
            else:
                error_label.config(text=f"Tabela {codigo} não criado!")
                error_label.place(x=0 ,y=screen_main_height-20)

        def edit():
            print('edit')

        clear()        
        label_ID = Label(main_frame, text="ID", bg='#dde', fg='#009', anchor=W)
        entry_ID = Entry(main_frame, relief=FLAT)
        label_ID.place(x=5,y=5, width=50, height=20)
        entry_ID.place(x=55,y=5, width=40, height=20)

        label_codigo = Label(main_frame, text="Codigo", bg='#dde', fg='#009', anchor=W)
        entry_codigo = Entry(main_frame, relief=FLAT)
        entry_codigo.bind("<Button>", clear_error)
        label_codigo.place(x=5,y=30, width=50, height=20)
        entry_codigo.place(x=55,y=30, width=40, height=20)

        label_contato = Label(main_frame, text="Contato", bg='#dde', fg='#009', anchor=W)
        entry_contato = Entry(main_frame, relief=FLAT)
        label_contato.place(x=5,y=70, width=50, height=20)
        entry_contato.place(x=55,y=70, width=40, height=20)

        label_telefone = Label(main_frame, text="Telefone", bg='#dde', fg='#009', anchor=W)
        entry_telefone = Entry(main_frame, relief=FLAT)
        label_telefone.place(x=5,y=95, width=50, height=20)
        entry_telefone.place(x=55,y=95, width=40, height=20)

        
        




        if opc == "new":
            button_save = Button(main_frame, text='Salvar', border=0, fg="#009", bg='white', command=save)
            button_save.place(x=100, y=5, width=100, height=20)
        if opc == "consult":
            button_edit = Button(main_frame, text='Editar', border=0, fg="#009", bg='white', command=edit)
            button_edit.place(x=100, y=5, width=100, height=20)
            entry_codigo.insert(0,"97002")
            entry_codigo.config(state= "disabled")



    db.check()
    db.execut("""CREATE TABLE IF NOT EXISTS "97002" (
                ID       INTEGER PRIMARY KEY ON CONFLICT
                         ROLLBACK AUTOINCREMENT NOT NULL
                         ON CONFLICT ROLLBACK,
                Contato  VARCHAR NOT NULL,
                Telefone VARCHAR NOT NULL
              );""")


    

    clear()
    




class Main(tk.Tk):
    def __init__(self, *args, **kwargs) -> None:
        self.window = Tk()
        self.window.title("Registro Prosoft")
        self.window.geometry(f'{screen_main_width}x{screen_main_height}')
        self.window.configure(bg='#dde')
        self.window.resizable(0, 0)
        
        self.menubar()
        self.main_frame = Frame(self.window, bg="#dde", borderwidth=0,relief=FLAT)
        self.main_frame.place(x=0, y=0, width=screen_main_width, height=screen_main_height-20)
        self.down_frame = Frame(self.window, bg="#fff", borderwidth=1,relief=FLAT)
        self.down_frame.place(x=0 ,y=screen_main_height-20, width=screen_main_width, height=20)
        self.erro_label = Label(self.down_frame, text="", fg="RED")
        self.erro_label.place(x=0 ,y=0)
        self.window.mainloop()

    def menubar(self):
        menu_bar  = Menu(self.window)
        opc_ticket = Menu(menu_bar, tearoff=False)
        opc_ticket.add_command(label = 'Novo' , command = lambda: self.ticket('new'))
        opc_ticket.add_command(label = 'Abrir', command = lambda: self.ticket('consult'))
        opc_ticket.add_separator()
        opc_ticket.add_command(label = "Fechar", command = self.window.quit)
        menu_bar.add_cascade(label = "Tickets", menu = opc_ticket)
        self.window.config(menu = menu_bar)

        Label(self.main_frame, text="Sem registo aberto", bg='#dde',
                fg='grey',anchor=W, font=('Calibri (Body)',15,'bold')
             ).place(x=( (screen_main_width/2) - (185/2) ) ,y=( (screen_main_height/2) - (20/2)))


    def ticket(self, opc):
        def clear(self):
            entry_ID        .delete(0, END)
            entry_codigo    .delete(0, END)
            entry_contato   .delete(0, END)
            entry_telefone  .delete(0, END)


        label_ID = Label(self.main_frame, text="ID", bg='#dde', fg='#009', anchor=W)
        entry_ID = Entry(self.main_frame, relief=FLAT)
        label_ID.place(x=5,y=5, width=50, height=20)
        entry_ID.place(x=55,y=5, width=40, height=20)

        label_codigo = Label(self.main_frame, text="Codigo", bg='#dde', fg='#009', anchor=W)
        entry_codigo = Entry(self.main_frame, relief=FLAT)
        label_codigo.place(x=5,y=30, width=50, height=20)
        entry_codigo.place(x=55,y=30, width=40, height=20)

        label_contato = Label(self.main_frame, text="Contato", bg='#dde', fg='#009', anchor=W)
        entry_contato = Entry(self.main_frame, relief=FLAT)
        label_contato.place(x=5,y=70, width=50, height=20)
        entry_contato.place(x=55,y=70, width=40, height=20)

        label_telefone = Label(self.main_frame, text="Telefone", bg='#dde', fg='#009', anchor=W)
        entry_telefone = Entry(self.main_frame, relief=FLAT)
        label_telefone.place(x=5,y=95, width=50, height=20)
        entry_telefone.place(x=55,y=95, width=40, height=20)

        button_ok = Button(self.main_frame, )


        entry_codigo.bind("<Button>", lambda x: self.erro_label.config(text=""))


app = Main()
