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

def add_reservation_menu():
    #==================================================choose_house===================================================================
    def choose_house():
        def add_reservation():
            #reservation info
            id_client = id_client_combobox.get()
            nemra_simana=ww.get()
            nemra_dar=sel.get()

            # Create Table
            if id_client and nemra_dar and nemra_simana:
                data_insert_query = '''INSERT INTO reservation(id_client,num_maison,num_semaine) VALUES (?, ?, ?)'''
                data_insert_tuple = (id_client,nemra_dar,nemra_simana)
                cursor.execute(data_insert_query, data_insert_tuple)
                sqlcon.commit()

                id_client_combobox.set('')
                num_maison_entry.set('')
                num_semaine_combobox.set('')

                tk.messagebox.showwarning(title= "success", message="Congratulation, your reservation has been successfully registered")

        #for widget in user_info_frame.winfo_children():
        #    if isinstance(widget, ttk.Combobox):
        #        widget.delete(0, 'end')
            else: 
                tk.messagebox.showwarning(title= "Error", message="all the informations are required")
        #--------------------------------------
        query = 'select num_maison from house'
        cursor.execute(query)
        houses = cursor.fetchall()
        for i in range(len(houses)):
            houses[i]=houses[i][0]

        sel = tk.StringVar()
        ww = tk.StringVar()
        def my_upd(*args):
            num_semaine_combobox.set('') # reset the
            query = "select num_semaine from reservation where num_maison='"+sel.get()+"'"
            cursor.execute(query)
            w = cursor.fetchall()
            for i in range(len(w)):
                w[i]=w[i][0]

            weeks=[]
            for j in range(10,41):
                if j not in w:
                    weeks.append(j)
            num_semaine_combobox['values']=weeks


            #global nemra_dar
            nemra_dar = sel.get()

        def my_upd2(*args):
            #global nemra_simana
            nemra_simana=ww.get()

        # le champ num_maison
        num_maison_label= tk.Label(user_info_frame,text="House name")
        num_maison_label.grid(row=2,column=0)
        num_maison_entry = ttk.Combobox(user_info_frame, values=houses,textvariable=sel, state="readonly")
        num_maison_entry.grid(row=3, column=0)
        # le champ num semaine
        num_semaine_label = tk.Label(user_info_frame, text="Weeks possible")
        num_semaine_combobox = ttk.Combobox(user_info_frame, values=sel,textvariable=ww, state="readonly")
        num_semaine_label.grid(row=2, column=1)
        num_semaine_combobox.grid(row=3, column=1)
        sel.trace('w',my_upd)
        ww.trace('w', my_upd2)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        #====
        button = tk.Button(frame, text="add_reservation", command=add_reservation)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    
    #===========================================choose weeek===================================================================
    def choose_week():
        def add_reservation():
            #reservation info
            id_client = id_client_combobox.get()
            nemra_dar=sel2.get()
            nemra_simana=sel.get()
            # Create Table
            if id_client and nemra_dar and nemra_simana:
                data_insert_query = '''INSERT INTO reservation(id_client,num_maison,num_semaine) VALUES (?, ?, ?)'''
                data_insert_tuple = (id_client,nemra_dar,nemra_simana)
                cursor.execute(data_insert_query, data_insert_tuple)
                sqlcon.commit()

                id_client_combobox.set('')
                num_house_combobox.set('')
                num_week_entry.set('')

                tk.messagebox.showwarning(title= "success", message="Congratulation, your reservation has been successfully registered")

        #for widget in user_info_frame.winfo_children():
        #    if isinstance(widget, ttk.Combobox):
        #        widget.delete(0, 'end')
            else: 
                tk.messagebox.showwarning(title= "Error", message="all the informations are required")
        #------------------------------------
        query = 'select num_maison from house'
        cursor.execute(query)
        houses = cursor.fetchall()
        for i in range(len(houses)):
            houses[i]=houses[i][0]
        houses.sort()
        sel = tk.StringVar()
        def my_upd(*args):
            #num_semaine_combobox.set('') # reset the
            query = "select num_maison from reservation where num_semaine='"+sel.get()+"'"
            cursor.execute(query)
            m = cursor.fetchall()
            for i in range(len(m)):
                m[i]=m[i][0]

            maison=[]
            for i in houses:
                if i not in m:
                    maison.append(i)
            
            num_house_combobox['values']=maison

            #global nemra_simana
            nemra_simana = sel.get()

        sel2 = tk.StringVar()
        def my_upd2(*args):
            #global nemra_dar
            nemra_dar=sel2.get()

    
        # le champ num_maison
        num_week_label= tk.Label(user_info_frame,text="Week number")
        num_week_label.grid(row=2,column=0)
        num_week_entry = ttk.Combobox(user_info_frame, values=[i for i in range(10,41)],textvariable=sel, state="readonly")
        num_week_entry.grid(row=3, column=0)
        # le champ num semaine
        num_house_label = tk.Label(user_info_frame, text="houses possible")
        num_house_combobox = ttk.Combobox(user_info_frame, values=sel, textvariable=sel2, state="readonly")
        num_house_label.grid(row=2, column=1)
        num_house_combobox.grid(row=3, column=1)
        sel.trace('w',my_upd)
        sel2.trace('w', my_upd2)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        #====
        button = tk.Button(frame, text="add_reservation", command=add_reservation)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)



    #------------------create window-----------------------------------
    

    frame = tk.Frame(main_frame)
    frame.pack()


    # Saving Maison Info
    user_info_frame =tk.LabelFrame(frame, text="Reservation Informations")
    user_info_frame.grid(row= 0, column=0, padx=20, pady=10)


    id_client_label= tk.Label(user_info_frame,text="id client")
    id_client_label.grid(row=0,column=0)
    query = 'select id_client from client'
    cursor.execute(query)
    result=cursor.fetchall()
    id_client_combobox = ttk.Combobox(user_info_frame,values=result, state="readonly")
    id_client_combobox.grid(row=1, column=0)


    text= tk.Label(user_info_frame,text="reserve by : ")
    text.grid(row=0, column=1)
    #-------------------------------------choose button-------------------------------------------

    choose=tk.StringVar()
    g1 = tk.Radiobutton(user_info_frame, text ="House", variable=choose, value="House", command=choose_house)
    g1.deselect()
    g1.grid(row=1, column=1)


    g2 = tk.Radiobutton(user_info_frame, text ="Week", variable=choose, value='Week', command=choose_week)
    g2.deselect()
    g2.grid(row=1, column=2)



    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)

    #window.mainloop()