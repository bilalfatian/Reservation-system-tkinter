import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import re
import sqlite3
from tkinter.messagebox import askyesno
from table_creation import *
from frams import *


def delete_client():
    def select_id_client():
        query = "select id_client from client"
        cursor.execute(query)
        all_id = cursor.fetchall()
        for i in range(len(all_id)):
            all_id[i]=all_id[i][0]
        return all_id

    all_id=select_id_client()
    frame = tk.Frame(main_frame)
    frame.pack()
    #id frame
    id_frame = tk.LabelFrame(frame, text="Id number")
    id_frame.grid(row= 0, column=0, padx=20, pady=10)
    #select an id
    
    id_label = tk.Label(id_frame, text="Enter the id number : ", padx=20, pady=10)
    id_label.grid(row=0, column=0)
    id_combobox =  ttk.Combobox(id_frame, values=all_id, state="readonly")
    id_combobox.grid(row=0, column=1)

    test=tk.Label(id_frame, text="                                       ", padx=20, pady=10)
    test.grid(row=0, column=2)
    
    def delete(id):
        answer = askyesno(title='confirmation', message='All the reservation made by this client will be canceled !\nconfirm the processe to delete this client')
        if answer:
            query = "delete from reservation where id_client={n}".format(n=id)
            cursor.execute(query)
            sqlcon.commit()
            query = "DELETE FROM client WHERE id_client={n}".format(n=id)
            cursor.execute(query)
            sqlcon.commit()

            id_combobox.set("")
            tk.messagebox.showinfo(title= "delete client", message=" Client information has been deleted successfully")
            all_id=select_id_client()
            id_combobox['values']=all_id


    button = tk.Button(frame, text="Delete client", command= lambda : delete(id_combobox.get()))
    button.grid(row=1, column=0, sticky="news", padx=20, pady=10)




def delete_house():
    def select_id_house():
        query = "select num_maison from house"
        cursor.execute(query)
        all_id = cursor.fetchall()
        for i in range(len(all_id)):
            all_id[i]=all_id[i][0]
        return all_id

    sel = tk.StringVar()
    def delete(id):
        answer = askyesno(title='confirmation', message='All the reservation made on this house will be canceled !\nconfirm the processe to delete this client')
        if answer:
            query = "delete from reservation where num_maison={n}".format(n=id)
            cursor.execute(query)
            sqlcon.commit()
            query = "DELETE FROM house WHERE num_maison={n}".format(n=id)
            cursor.execute(query)
            sqlcon.commit()
            id_combobox.set("")
            tk.messagebox.showinfo(title= "delete house", message=" House information has been deleted successfully")
            all_id=select_id_house()
            id_combobox['values']=all_id
            


    all_id=select_id_house()
    frame = tk.Frame(main_frame)
    frame.pack()
    #id frame
    id_frame = tk.LabelFrame(frame, text="Id number")
    id_frame.grid(row= 0, column=0, padx=20, pady=10)
    #select an id
    
    id_label = tk.Label(id_frame, text="Enter the id number : ", padx=20, pady=10)
    id_label.grid(row=0, column=0)
    id_combobox =  ttk.Combobox(id_frame, values=all_id, state="readonly")
    id_combobox.grid(row=0, column=1)

    test=tk.Label(id_frame, text="                                       ", padx=20, pady=10)
    test.grid(row=0, column=2)

    button = tk.Button(frame, text="Delete house",command =lambda : delete(id_combobox.get()))
    button.grid(row=1, column=0, sticky="news", padx=20, pady=10)
    
def delete_reservation():
    def select_id_reservation():
        query = "select num_reservation from reservation"
        cursor.execute(query)
        all_id = cursor.fetchall()
        for i in range(len(all_id)):
            all_id[i]=all_id[i][0]
        return all_id

    def delete(id):
        answer = askyesno(title='confirmation', message='confirm the processe to cancel this reservation')
        if answer:
            query = "delete from reservation where num_reservation={n}".format(n=id)
            cursor.execute(query)
            sqlcon.commit()

            id_combobox.set("")
            tk.messagebox.showinfo(title= "delete house", message=" reservation been canceled successfully")

            all_id=select_id_reservation()
            id_combobox['values']=all_id
            


    all_id=select_id_reservation()
    frame = tk.Frame(main_frame)
    frame.pack()
    #id frame
    id_frame = tk.LabelFrame(frame, text="Id number")
    id_frame.grid(row= 0, column=0, padx=20, pady=10)
    #select an id
    
    id_label = tk.Label(id_frame, text="Enter the id number : ", padx=20, pady=10)
    id_label.grid(row=0, column=0)
    id_combobox =  ttk.Combobox(id_frame, values=all_id, state="readonly")
    id_combobox.grid(row=0, column=1)

    test=tk.Label(id_frame, text="                                       ", padx=20, pady=10)
    test.grid(row=0, column=2)

    button = tk.Button(frame, text="Cancel reservation",command =lambda : delete(id_combobox.get()))
    button.grid(row=1, column=0, sticky="news", padx=20, pady=10)