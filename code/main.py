import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import re
import sqlite3

from table_creation import *
from add_client import *
from add_house import *
from add_reservation import *
from update_client import *
from update_house import *
from update_reservation import *
from delete import *
from frams import *





def add_search_menu():
    True


def hide_frame(fr):
    for widget in fr.winfo_children():
        widget.place_forget()


def delete_pages():
    for frame in main_frame.winfo_children():
        frame.destroy()


## make an indicated to the menu selected
def indicate(lb):
    hide_indicators()
    lb.config(bg='#185aff')
    delete_pages()


## hide all indicators
def hide_indicators():
    client_indicate.config(bg='#c3c3c3')
    house_indicate.config(bg='#c3c3c3')
    reservation_indicate.config(bg='#c3c3c3')
    search_indicate.config(bg='#c3c3c3')



## indicate
client_indicate=tk.Label(options_frame,text='',bg='#c3c3c3')
house_indicate=tk.Label(options_frame,text='',bg='#c3c3c3')
reservation_indicate=tk.Label(options_frame,text='',bg='#c3c3c3')
search_indicate=tk.Label(options_frame,text='',bg='#c3c3c3')



#botons
client_btn = tk.Button(options_frame, text='Client', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3',
                    command=lambda: [indicate(client_indicate),client_clicked()])
client_btn.place(x=10, y=50)

house_btn = tk.Button(options_frame, text='House', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3',
                    command=lambda: [indicate(house_indicate),house_clicked()])
house_btn.place(x=10, y=100)

reservation_btn = tk.Button(options_frame, text='Reservation', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3',
                    command=lambda: [indicate(reservation_indicate), reservation_clicked()])
reservation_btn.place(x=10, y=150)

search_btn = tk.Button(options_frame, text='Search', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3',
                    command=lambda: [indicate(search_indicate),search_clicked()])
search_btn.place(x=10, y=200)


#options buttons

add_client_btn = tk.Button(options_frame, text='Add Client', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda: [delete_pages(), add_client_menu()] )
add_house_btn = tk.Button(options_frame, text='Add House', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), add_house_menu()] )
add_reservation_btn = tk.Button(options_frame, text='Add Reservation', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), add_reservation_menu()] )

update_client_btn = tk.Button(options_frame, text='Update Client', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), update_client_menu()] )
update_house_btn = tk.Button(options_frame, text='Update House', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), update_house_menu()] )
update_reservation_btn = tk.Button(options_frame, text='Update Reservation', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), update_reservation()] )

delete_client_btn = tk.Button(options_frame, text='Delete Client', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), delete_client()] )
delete_house_btn = tk.Button(options_frame, text='Delete House', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), delete_house()] )
delete_reservation_btn = tk.Button(options_frame, text='Delete Reservation', font=('Bold',13),
                    fg='#158aff', bd=0, bg='#c3c3c3', command=lambda:[delete_pages(), delete_reservation()] )




#mise en page
def client_clicked():
    hide_frame(options_frame)
    client_btn.place(x=10, y=50)

    add_client_btn.place(x=30, y=85)
    update_client_btn.place(x=30, y=120)
    delete_client_btn.place(x=30, y=155)

    house_btn.place(x=10, y=205)
    reservation_btn.place(x=10, y=255)
    search_btn.place(x=10, y=305)

    client_indicate.place(x=3, y=50, width=5, height=30)
    house_indicate.place(x=3, y=205, width=5, height=30)
    reservation_indicate.place(x=3, y=255, width=5, height=30)
    search_indicate.place(x=3, y=305, width=5, height=30)

def house_clicked():
    hide_frame(options_frame)
    client_btn.place(x=10, y=50)
    house_btn.place(x=10, y=100)

    add_house_btn.place(x=30, y=135)
    update_house_btn.place(x=30, y=170)
    delete_house_btn.place(x=30, y=205)

    reservation_btn.place(x=10, y=255)
    search_btn.place(x=10, y=305)

    client_indicate.place(x=3, y=50, width=5, height=30)
    house_indicate.place(x=3, y=100, width=5, height=30)
    reservation_indicate.place(x=3, y=255, width=5, height=30)
    search_indicate.place(x=3, y=305, width=5, height=30)

def reservation_clicked():
    hide_frame(options_frame)
    client_btn.place(x=10, y=50)
    house_btn.place(x=10, y=100)
    reservation_btn.place(x=10, y=150)

    add_reservation_btn.place(x=30, y=185)
    update_reservation_btn.place(x=30, y=220)
    delete_reservation_btn.place(x=30, y=255)

    search_btn.place(x=10, y=305)

    client_indicate.place(x=3, y=50, width=5, height=30)
    house_indicate.place(x=3, y=100, width=5, height=30)
    reservation_indicate.place(x=3, y=150, width=5, height=30)
    search_indicate.place(x=3, y=305, width=5, height=30)

def search_clicked():
    hide_frame(options_frame)
    client_btn.place(x=10, y=50)
    house_btn.place(x=10, y=100)
    reservation_btn.place(x=10, y=150)
    search_btn.place(x=10, y=200)

    client_indicate.place(x=3, y=50, width=5, height=30)
    house_indicate.place(x=3, y=100, width=5, height=30)
    reservation_indicate.place(x=3, y=150, width=5, height=30)
    search_indicate.place(x=3, y=200, width=5, height=30)




#------------main---------------
root.mainloop()

query = 'select * from client'
cursor.execute(query)
res = cursor.fetchall()
#print(res)

query = 'select * from house'
cursor.execute(query)
res = cursor.fetchall()
#print(res)

query = 'select * from reservation'
cursor.execute(query)
res = cursor.fetchall()
#print(res)



sqlcon.close()



