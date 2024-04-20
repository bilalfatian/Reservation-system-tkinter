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




def update_house_menu():
    ## connect the add client with the data base
    
    #---------------------------changing interface-------------------------------------------
    def selected(event):
        def updat_house():
            nom_maison = nom_maison_entry.get()
            nombre_chambre = nombre_chambre_spinbox.get()
            Adresse = Adresse_entry.get()
            prix = prix_entry.get()
            nb_max_personnes = nb_max_personnes_spinbox.get()
            comment = comentaire_entry.get(1.0, "end-1c")
            if nom_maison and nombre_chambre and Adresse and prix and nb_max_personnes:
                #if number of room integer
                try:
                    int(nombre_chambre)
                except ValueError:
                    tk.messagebox.showwarning(title= "Error", message="The number of rooms must be integer")
                    return
                #if price is integer
                try:
                    int(prix)
                except ValueError:
                    tk.messagebox.showwarning(title= "Error", message="The price must be integer")
                    return
                #if nb_max_personnes integer
                try:
                    int(nb_max_personnes)
                except ValueError:
                    tk.messagebox.showwarning(title= "Error", message="The maximum number of people must be integer")
                    return
                #if the price more than nb_rooms*100
                x=int(nombre_chambre)
                y=int(prix)
                min_price=100*x
                if y<100*x:
                    tk.messagebox.showwarning(title= "Error", message="the price must be at least {n}".format(n=min_price))
                    return

                answer = askyesno(title='confirmation', message='Are you sure that you want to update?')
                if answer:
                    data_insert_query = '''Update house set nom_maison = ?, nombre_chambre  = ?, Adresse = ?, prix = ?, nb_max_personnes = ?, comment = ? where num_maison = ?'''
                    data_insert_tuple = (nom_maison, nombre_chambre, Adresse, prix, nb_max_personnes, comment, id)
                    (cursor.execute(data_insert_query, data_insert_tuple))
                    sqlcon.commit()

                    tk.messagebox.showwarning(title= "update house information", message=" The update has been made successfully ")
                    id_combobox.set('')
                    house_info_frame.grid_forget()
                    more_house_info_frame.grid_forget()
                    button.grid_forget()
            

            else:
                tk.messagebox.showwarning(title="Error", message="       missing case\n\n       update failure.")





        #---------------------------------------------------------------------------------

        
        # Selecting old values from the client table
        id=event.widget.get()

        query = "select * from house where num_maison='"+str(id)+"'"
        cursor.execute(query)
        res = cursor.fetchall()
        

        house_info_frame =tk.LabelFrame(frame, text="house Informations")
        #house_info_frame.configure(bg="#fff")
        house_info_frame.grid(row= 1, column=0, padx=20, pady=10)
        #le champ nom_maison
        nom_maison_label = tk.Label(house_info_frame, text="house name")
        nom_maison_label.grid(row=0, column=0)
        nom_maison_entry = tk.Entry(house_info_frame)
        nom_maison_entry.insert(END, res[0][1])
        nom_maison_entry.grid(row=1, column=0)
        # le champ nombre de chambres
        var = IntVar()
        nombre_chambre_label = tk.Label(house_info_frame, text="number of rooms")
        nombre_chambre_spinbox = tk.Spinbox(house_info_frame, from_=1, to=10, textvariable=var)
        var.set(res[0][2])
        nombre_chambre_label.grid(row=0, column=1)
        nombre_chambre_spinbox.grid(row=1, column=1)
        #le champ Adresse nb_personnes_max
        var=IntVar()
        nb_max_personnes_label = tk.Label(house_info_frame, text="Maximum number of people")
        nb_max_personnes_label.grid(row=0, column=2)
        nb_max_personnes_spinbox = tk.Spinbox(house_info_frame,from_=1, to=10,textvariable=var)
        var.set(res[0][5])
        nb_max_personnes_spinbox.grid(row=1, column=2)
        # le champ Adresse
        Adresse_label = tk.Label(house_info_frame, text="Address")
        Adresse_label.grid(row=2, column=0)
        Adresse_entry = tk.Entry(house_info_frame)
        Adresse_entry.insert(END, res[0][3])
        Adresse_entry.grid(row=3, column=0)
        # le champ Prix
        prix_label = tk.Label(house_info_frame, text="Price")
        prix_label.grid(row=2, column=1)
        prix_entry = tk.Entry(house_info_frame)
        prix_entry.insert(END, res[0][4])
        prix_entry.grid(row=3, column=1)

        # le champ de comentaire--------------------------------
        more_house_info_frame =tk.LabelFrame(frame, text="About house")
        more_house_info_frame.grid(row= 2, column=0, padx=20, pady=10)


        #house description
        comentaire_label = tk.Label(more_house_info_frame, text="description of the house")
        comentaire_label.grid(row=0, column=0)
        comentaire_entry = tk.Text(more_house_info_frame, height=3, width=33)
        comentaire_entry.insert(END, res[0][6])
        comentaire_entry.grid(row=0, column=1)
        #---scrollbar for comentaire
        scrollbar1=ttk.Scrollbar(more_house_info_frame, orient='vertical', command=comentaire_entry.yview)
        scrollbar1.grid(row=0, column=2, sticky=tk.NS)
        comentaire_entry['yscrollcommand']=scrollbar1.set




        #############
        for widget in house_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)
        #############
        for widget in more_house_info_frame.winfo_children():
            widget.grid_configure(padx=10, pady=5)

        # Button
        button = tk.Button(frame, text="update data", command= updat_house)
        button.grid(row=3, column=0, sticky="news", padx=20, pady=10)

    frame = tk.Frame(main_frame)
    frame.pack()
    # Selecting all the clients id
    query = "select num_maison from house"
    cursor.execute(query)
    all_house_id = cursor.fetchall()
    for i in range(len(all_house_id)):
        all_house_id[i]=all_house_id[i][0]


    #id frame
    id_house_frame = tk.LabelFrame(frame, text="house number")
    id_house_frame.grid(row= 0, column=0, padx=20, pady=10)
    #select an id
    

    id_label = tk.Label(id_house_frame, text="Enter the house number : ", padx=20, pady=10)
    id_label.grid(row=0, column=0)
    id_combobox =  ttk.Combobox(id_house_frame, values=all_house_id, state="readonly")
    id_combobox.grid(row=0, column=1)

    test=tk.Label(id_house_frame, text="    ", padx=70, pady=10)
    test.grid(row=0, column=2)

    id_combobox.current()
    id_combobox.bind("<<ComboboxSelected>>", selected)
    # Saving User Info