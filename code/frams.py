import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import pandas as pd
import numpy as np
import re
import sqlite3


root = tk.Tk()
root.geometry('500x400')
root.title('best data base in the world')


## Siting the left frame
options_frame = tk.Frame(root, bg='#c3c3c3')
options_frame.pack(side=tk.LEFT)
options_frame.pack_propagate(False)
options_frame.configure(width=180, height=1000)

## Siting the black cadre
main_frame = tk.Frame(root, highlightbackground='black',
                        highlightthickness=2)
main_frame.pack(side=tk.LEFT)
main_frame.pack_propagate(False)
main_frame.configure(height=1000, width=1500)