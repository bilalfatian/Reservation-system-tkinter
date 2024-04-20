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

def update_client_menu():
    ## connect the add client with the data base
    
    #---------------------------changing interface-------------------------------------------
    def selected(event):
        def updat_client():
            firstname = first_name_entry.get()
            lastname = last_name_entry.get()
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            phone = phone_number_entry.get()
            email_adresse = email_entry.get()
            address=address_entry.get()

            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
            if not(re.fullmatch(regex, email_adresse)):
                tk.messagebox.showwarning(title= "New client", message=" email not accepted ")

            else:
                if firstname and lastname and title and age and nationality and phone and email_adresse:
                    answer = askyesno(title='confirmation', message='Are you sure that you want to update?')
                    if answer:
                        # Insert Data
                        data_insert_query = 'Update client set firstname = ?, lastname = ?, title = ?, age = ?, address = ?, nationality = ?, phone_number = ?, email = ? where id_client = ?'
                        data_insert_tuple = (firstname, lastname, title, int(age), address, nationality, phone, email_adresse, id)
                        (cursor.execute(data_insert_query, data_insert_tuple))
                        sqlcon.commit()

                        tk.messagebox.showwarning(title= "update client information", message=" The update has been made successfully ")
                        id_combobox.set('')
                        user_info_frame.grid_forget()
                        button.grid_forget()


                
                else:
                    tk.messagebox.showwarning(title="Error", message="       missing case\n\n       update failure.")
            






        #---------------------------------------------------------------------------------
        # Selecting old values from the client table
        id=event.widget.get()

        query = "select * from client where id_client='"+str(id)+"'"
        cursor.execute(query)
        res = cursor.fetchall()
        

        user_info_frame =tk.LabelFrame(frame, text="User Information")
        user_info_frame.grid(row= 1, column=0, padx=20, pady=10)

        first_name_label = tk.Label(user_info_frame, text="First Name")
        first_name_label.grid(row=0, column=0)
        last_name_label = tk.Label(user_info_frame, text="Last Name")
        last_name_label.grid(row=0, column=1)

        first_name_entry = tk.Entry(user_info_frame)
        first_name_entry.insert(END, res[0][1])
        last_name_entry = tk.Entry(user_info_frame)
        last_name_entry.insert(END, res[0][2])
        first_name_entry.grid(row=1, column=0)
        last_name_entry.grid(row=1, column=1)

        title_label = tk.Label(user_info_frame, text="Title")
        title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."],state="readonly")
        title_combobox.set(str(res[0][3]))
        title_label.grid(row=0, column=2)
        title_combobox.grid(row=1, column=2)

        age_label = tk.Label(user_info_frame, text="Age")
        age_spinbox = ttk.Combobox(user_info_frame, values=[i for i in range(18,120)], state="readonly")
        age_spinbox.set(str(res[0][4]))
        age_label.grid(row=0, column=3)
        age_spinbox.grid(row=1, column=3)

        address_label = tk.Label(user_info_frame, text="Address")
        address_entry = tk.Entry(user_info_frame)
        address_entry.insert(END, res[0][5])
        address_label.grid(row=2, column=0)
        address_entry.grid(row=3, column=0)

        nationality_label = tk.Label(user_info_frame, text="Nationality")
        nationality_combobox = ttk.Combobox(user_info_frame, values=country, state="readonly")
        nationality_combobox.set(str(res[0][6]))
        nationality_label.grid(row=2, column=1)
        nationality_combobox.grid(row=3, column=1)

        phone_number_label = tk.Label(user_info_frame, text="Phone Number")
        phone_number_label.grid(row=2, column=2)
        phone_number_entry =  tk.Entry(user_info_frame)
        phone_number_entry.insert(END, res[0][7])
        phone_number_entry.grid(row=3, column=2)

        email_label = tk.Label(user_info_frame, text="Email")
        email_label.grid(row=2, column=3)
        email_entry = tk.Entry(user_info_frame)
        email_entry.insert(END, res[0][8])
        email_entry.grid(row=3, column=3)

        for widget in user_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Button
        button = tk.Button(frame, text="update data", command= updat_client)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

        frame.pack(pady=20)

    frame = tk.Frame(main_frame)
    frame.pack()
    # Selecting all the clients id
    query = "select id_client from client"
    cursor.execute(query)
    all_id = cursor.fetchall()
    for i in range(len(all_id)):
        all_id[i]=all_id[i][0]


    #id frame
    id_frame = tk.LabelFrame(frame, text="Id number")
    id_frame.grid(row= 0, column=0, padx=20, pady=10)
    #select an id
    

    id_label = tk.Label(id_frame, text="Enter the id number : ", padx=20, pady=10)
    id_label.grid(row=0, column=0)
    id_combobox =  ttk.Combobox(id_frame, values=all_id, state="readonly")
    id_combobox.grid(row=0, column=1)

    test=tk.Label(id_frame, text="                                                               ", padx=70, pady=10)
    test.grid(row=0, column=2)

    id_combobox.current()
    id_combobox.bind("<<ComboboxSelected>>", selected)
    # Saving User Info