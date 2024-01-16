#############################
# Training (Menu)
# JCY oct 23
# PRO DB PY
#############################

"""
Author: Blinar Fetiu
File: menu.py (Exercise)
Module: ProjDBPY
Date: 02.01.2023
"""

import mysql.connector
import tkinter as tk
from database import *
from displayresults import display_results_level1, display_results_level2, login_window, attempt_login, logged_in, changepermissions_window, user_level
import geo01
import info02
import info05
import hashlib


# Function to log out
def logout():
    global gameswindow
    gameswindow.destroy()
    login_window()


open_dbconnection()

# exercises array
a_exercise=["geo01", "info02", "info05"]
albl_image=[None, None, None] # label (with images) array
a_image=[None, None, None] # images array
a_title=[None, None, None] # array of title (ex: GEO01)

dict_games = {"geo01": geo01.open_window_geo_01, "info02": info02.open_window_info_02, "info05": info05.open_window_info_05}



# call other windows (exercices)
def exercise(event, exer):
    dict_games[exer](gameswindow)


# Start with the login window
login_window()

# Create the infinite loop
infinite_loop = True

while infinite_loop:
    # Function to display the games etc.
    if logged_in() == True:

        # Main window
        gameswindow = tk.Tk()
        gameswindow.title("Training, entrainement cérébral")
        gameswindow.geometry("1100x900")

        # Bind the on_closing function to the window closing event
        gameswindow.protocol("WM_DELETE_WINDOW", quit)

        # color définition
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color # translation in hexa
        gameswindow.configure(bg=hex_color)
        gameswindow.grid_columnconfigure((0, 1, 2), minsize=300, weight=1)

        # Title création
        lbl_title = tk.Label(gameswindow, text="TRAINING MENU", font=("Arial", 15))
        lbl_title.grid(row=0, column=1, ipady=5, padx=40, pady=40)

        # labels creation and positioning
        for ex in range(len(a_exercise)):
            a_title[ex]=tk.Label(gameswindow, text=a_exercise[ex], font=("Arial", 15))
            a_title[ex].grid(row=1+2*(ex//3), column=ex % 3, padx=40, pady=10) # 3 label per row

            a_image[ex] = tk.PhotoImage(file="img/" + a_exercise[ex] + ".gif") # image name
            albl_image[ex] = tk.Label(gameswindow, image=a_image[ex]) # put image on label
            albl_image[ex].grid(row=2 + 2*(ex // 3), column=ex % 3, padx=40, pady=10) # 3 label per row
            albl_image[ex].bind("<Button-1>", lambda event, ex = ex: exercise(event=None, exer=a_exercise[ex])) # link to others .py
            print(a_exercise[ex])

        # If users permission level is 1
        if user_level() == True:
            # Buttons, display results & quit
            btn_display = tk.Button(gameswindow, text="Display results", font=("Arial", 15))
            btn_display.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
            btn_display.bind("<Button-1>", lambda e: display_results_level1(e))
        else:
            # Buttons, display results & quit
            btn_display = tk.Button(gameswindow, text="Display results", font=("Arial", 15))
            btn_display.grid(row=1 + 2 * len(a_exercise) // 3, column=1)
            btn_display.bind("<Button-1>", lambda e: display_results_level2(e))
            # Buttons, display results & quit
            btn_changepermissions = tk.Button(gameswindow, text="Change permissions", font=("Arial", 15))
            btn_changepermissions.grid(row=2 + 2 * len(a_exercise) // 3, column=1)
            btn_changepermissions.bind("<Button-1>", lambda e: changepermissions_window())

        btn_finish = tk.Button(gameswindow, text="Logout", font=("Arial", 15), command=logout)
        btn_finish.grid(row=3 + 2 * len(a_exercise) // 3, column=1)

        # main loop
        gameswindow.mainloop()

close_dbconnection()


