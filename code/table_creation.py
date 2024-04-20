import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import re
import sqlite3


#connecting with the data base
sqlcon = sqlite3.connect(r"path-to-your-project\project\test.db")
sqlcon.execute("PRAGMA foreign_keys = 1")
cursor = sqlcon.cursor()

#tables creatation
client_table = '''CREATE TABLE IF NOT EXISTS client 
            (id_client INTEGER PRIMARY KEY, firstname TEXT, lastname TEXT, title TEXT, age INT, address, nationality TEXT, 
            phone_number TEXT UNIQUE, email INT UNIQUE)
            '''
cursor.execute(client_table)

house_table = '''CREATE TABLE IF NOT EXISTS house(num_maison INTEGER PRIMARY KEY,nom_maison TEXT UNIQUE,
                            nombre_chambre INT,Adresse TEXT UNIQUE,prix INT CHECK(prix >= 100*nombre_chambre),
                            nb_max_personnes INT, comment TEXT);'''
sqlcon.execute(house_table)

table_create_query = '''CREATE TABLE IF NOT EXISTS reservation(num_reservation INTEGER primary key,id_client INT,num_maison INT,
                            num_semaine INT,
                            FOREIGN KEY (id_client) REFERENCES client (id_client), 
                            FOREIGN KEY (num_maison) REFERENCES house (num_maison)); '''
sqlcon.execute(table_create_query)


# creating two tables with all countries and their code numbers in the world
df = pd.read_json("path-to-your-project/project/countryPhoneCodes.json")
country = np.array(df['country'])
code = np.array(df['code'])

L = []
for i in range(len(country)):
    L.append(country[i])
country = L