import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import re
import sqlite3

from frams import *
from table_creation import *

def add_client_menu():
    ## connect the add client with the data base
    def add_client():

        if 1:
            # User info
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
                    

                    # Insert Data
                    data_insert_query = 'INSERT INTO client (firstname, lastname, title, age, address, nationality, phone_number, email) VALUES (?, ?, ?, ?, ?, ?, ?, ?)'
                    data_insert_tuple = (firstname, lastname, title, age, address, nationality, phone, email_adresse)

                    success_flg = True
                    try:
                        (cursor.execute(data_insert_query, data_insert_tuple))
                    except:
                        success_flg = False

                    if success_flg == False:
                        tk.messagebox.showwarning(title= "New client", message=" email or phone number already existe ")
                    else:
                        tk.messagebox.showwarning(title= "New client", message=" The entry has been made successfully ")
                
                    sqlcon.commit()
               
                else:
                    tk.messagebox.showwarning(title="Error", message="missing case.")
        else:
            tk.messagebox.showwarning(title= "Error", message="You have not accepted the terms")
    

    frame = tk.Frame(main_frame)
    frame.pack()

    # Saving User Info
    user_info_frame =tk.LabelFrame(frame, text="User Information")
    user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

    first_name_label = tk.Label(user_info_frame, text="First Name")
    first_name_label.grid(row=0, column=0)
    last_name_label = tk.Label(user_info_frame, text="Last Name")
    last_name_label.grid(row=0, column=1)

    first_name_entry = tk.Entry(user_info_frame)
    last_name_entry = tk.Entry(user_info_frame)
    first_name_entry.grid(row=1, column=0)
    last_name_entry.grid(row=1, column=1)

    title_label = tk.Label(user_info_frame, text="Title")
    title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
    title_label.grid(row=0, column=2)
    title_combobox.grid(row=1, column=2)

    age_label = tk.Label(user_info_frame, text="Age")
    age_spinbox = tk.Spinbox(user_info_frame, from_=18, to=110)
    age_label.grid(row=0, column=3)
    age_spinbox.grid(row=1, column=3)

    address_label = tk.Label(user_info_frame, text="Address")
    address_entry = tk.Entry(user_info_frame)
    address_label.grid(row=2, column=0)
    address_entry.grid(row=3, column=0)

    nationality_label = tk.Label(user_info_frame, text="Nationality")
    nationality_combobox = ttk.Combobox(user_info_frame, values=country)
    nationality_label.grid(row=2, column=1)
    nationality_combobox.grid(row=3, column=1)

    phone_number_label = tk.Label(user_info_frame, text="Phone Number")
    phone_number_label.grid(row=2, column=2)
    phone_number_entry =  tk.Entry(user_info_frame)
    phone_number_entry.grid(row=3, column=2)

    email_label = tk.Label(user_info_frame, text="Email")
    email_label.grid(row=2, column=3)
    email_entry = tk.Entry(user_info_frame)
    email_entry.grid(row=3, column=3)

    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)


    

    # Button
    button = tk.Button(frame, text="Enter data", command= add_client)
    button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    frame.pack(pady=20)