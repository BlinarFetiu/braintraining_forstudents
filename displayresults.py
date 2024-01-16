"""
Author: Blinar Fetiu
File: displayresults
Module: ProjDBPY
Date: 02.01.2023
"""

import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import *
from datetime import time, timedelta
import hashlib


# Define logged in variable already in case the user closes the window immediately to avoid errors
return_value = False


# Function for the creation of the login window
def login_window():
    global loginwindow, login

    # Login window
    loginwindow = tk.Tk()
    loginwindow.title("Login")
    loginwindow.geometry("350x260")

    # Bind the on_closing function to the window closing event
    loginwindow.protocol("WM_DELETE_WINDOW", quit)

    # Window canvas
    canvas_login = tk.Canvas(loginwindow, width=2000, height=500)
    canvas_login.grid(row=0, column=0, padx=5, pady=5, columnspan=3, rowspan=6)

    # Labels and entries
    login_pseudo = tk.Label(canvas_login, text="Pseudo:", font=("Arial", 10), width=15)
    login_pseudo.grid(row=1, column=0, ipady=5, padx=0, pady=5)
    login_pseudo_entry = tk.Entry(canvas_login, width=15)
    login_pseudo_entry.grid(row=1, column=2, ipady=5, padx=0, pady=5)

    login_password = tk.Label(canvas_login, text="Password:", font=("Arial", 10), width=15)
    login_password.grid(row=2, column=0, ipady=5, padx=0, pady=5)
    login_password_entry = tk.Entry(canvas_login, width=15, show="*")  # Use show="*" to hide the password
    login_password_entry.grid(row=2, column=2, ipady=5, padx=0, pady=5)

    space = tk.Label(canvas_login, text=" ", font=("Arial", 10), width=15)
    space.grid(row=3, column=0, ipady=5, padx=0, pady=5)

    btn_login = tk.Button(canvas_login, text="Login", command=lambda: attempt_login(login_pseudo_entry.get(), login_password_entry.get()), width=10, height=1)
    btn_login.grid(row=4, column=1, pady=5, padx=10)

    btn_register = tk.Button(canvas_login, text="Register", command=register_window, width=10, height=1)
    btn_register.grid(row=5, column=1, pady=5, padx=10)

    btn_register = tk.Button(canvas_login, text="Quit", command=quit, width=10, height=1)
    btn_register.grid(row=6, column=1, pady=5, padx=10)

    # main loop
    loginwindow.mainloop()


# Verify the login data
def attempt_login(username, password):
    global login, users_level, users_name, return_value

    # Get the name to save time with the name in exercises etc.
    users_name = username
    if verify_password(username, password):
        # Get users level
        users_level = get_users_level(username)[0]
        username = users_name
        user_level()
        users_pseudo()
        return_value = True
        loginwindow.destroy()
    else:
        messagebox.showinfo("Info", "Invalid username or password")
        return_value = False

    # Confirm the users login
    logged_in()
    return users_name


# Function to confirm users permission level
def user_level():
    global users_level
    if users_level == 1:
        return True


# Function to confirm users name
def users_pseudo():
    global users_name
    return users_name


# Function to confirm the fact that the user has logged in
def logged_in():
    global return_value
    if return_value == True:
        return True
        return_value = False
    else:
        return False


# Function for the creation of the register window
def register_window():
    global loginwindow, register_pseudo, register_password_entry, registerwindow

    # Destroy the login window to avoid confusion
    loginwindow.destroy()

    # Login window
    registerwindow = tk.Tk()
    registerwindow.title("Register")
    registerwindow.geometry("350x210")

    # Bind the on_closing function to the window closing event
    registerwindow.protocol("WM_DELETE_WINDOW", quit)

    # Window canvas
    canvas_register = tk.Canvas(registerwindow, width=2000, height=500)
    canvas_register.grid(row=0, column=0, padx=5, pady=5, columnspan=3, rowspan=5)

    # Labels and entries
    register_pseudo = tk.Label(canvas_register, text="Pseudo:", font=("Arial", 10), width=15)
    register_pseudo.grid(row=1, column=0, ipady=5, padx=0, pady=5)
    register_pseudo = tk.Entry(canvas_register, width=15)
    register_pseudo.grid(row=1, column=2, ipady=5, padx=0, pady=5)

    register_password = tk.Label(canvas_register, text="Password:", font=("Arial", 10), width=15)
    register_password.grid(row=2, column=0, ipady=5, padx=0, pady=5)
    register_password_entry = tk.Entry(canvas_register, width=15, show="*")
    register_password_entry.grid(row=2, column=2, ipady=5, padx=0, pady=5)

    space = tk.Label(canvas_register, text=" ", font=("Arial", 10), width=15)
    space.grid(row=3, column=0, ipady=5, padx=0, pady=5)

    btn_register = tk.Button(canvas_register, text="Register", command=register_user, width=10, height=1)
    btn_register.grid(row=4, column=1, pady=5, padx=10)
    btn_back = tk.Button(canvas_register, text="Back", command=lambda: [registerwindow.destroy(), login_window()], width=10, height=1)
    btn_back.grid(row=5, column=1, pady=5, padx=10)

    # main loop
    registerwindow.mainloop()


# Function to verify users existence and add him/her to the database
def register_user():
    # Get values
    pseudo = register_pseudo.get()
    password = register_password_entry.get()

    if check_name(pseudo) == None:
        # Hash the password
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        # Set the first letter to uppercase
        pseudo = pseudo.capitalize()
        # Insert user into the database
        add_student(pseudo, hashed_password)
        # Inform the user
        messagebox.showinfo("Info", "User registered successfully")
        # Close the window and make the user log in
        registerwindow.destroy(); login_window()

    else:
        print("This user already exists")


# Function for the creation of the register window
def changepermissions_window():
    global changepermissions_name_entry, changepermissions_level_entry, changepermissions_window

    # Login window
    changepermissions_window = tk.Tk()
    changepermissions_window.title("Register")
    changepermissions_window.geometry("450x210")

    # Window canvas
    canvas_changepermissions = tk.Canvas(changepermissions_window, width=2000, height=500)
    canvas_changepermissions.grid(row=0, column=0, padx=5, pady=5, columnspan=3, rowspan=5)

    # Labels and entries
    changepermissions_name = tk.Label(canvas_changepermissions, text="Pseudo:", font=("Arial", 10), width=20)
    changepermissions_name.grid(row=1, column=0, ipady=5, padx=0, pady=5)
    changepermissions_name_entry = tk.Entry(canvas_changepermissions, width=21)
    changepermissions_name_entry.grid(row=1, column=2, ipady=5, padx=0, pady=5)

    changepermissions_level = tk.Label(canvas_changepermissions, text="Change permission to:", font=("Arial", 10), width=20)
    changepermissions_level.grid(row=2, column=0, ipady=5, padx=0, pady=5)
    changepermissions_level_entry = tk.Entry(canvas_changepermissions, width=21)
    changepermissions_level_entry.grid(row=2, column=2, ipady=5, padx=0, pady=5)

    space = tk.Label(canvas_changepermissions, text=" ", font=("Arial", 10), width=15)
    space.grid(row=3, column=0, ipady=5, padx=0, pady=5)

    btn_register = tk.Button(canvas_changepermissions, text="Change permission", command=update_users_permissionlevel, width=15, height=1)
    btn_register.grid(row=4, column=1, pady=5, padx=10)
    btn_back = tk.Button(canvas_changepermissions, text="Back", command=changepermissions_window.destroy, width=10, height=1)
    btn_back.grid(row=5, column=1, pady=5, padx=10)

    # main loop
    changepermissions_window.mainloop()


# Function to update users permission level
def update_users_permissionlevel():
    # Get values
    user = changepermissions_name_entry.get()
    level = changepermissions_level_entry.get()
    # Get users ID
    user_id = get_studentId(user)
    if user_id == None:
        messagebox.showinfo("Info", "This user doesn't exist")
    else:
        if level == "1" or level == "2":
            update_permission(level, user_id[0])
            messagebox.showinfo("Info", "Users permission updated")
            changepermissions_window.destroy()
        else:
            messagebox.showinfo("Info", "The level must be 1 (student) or 2 (teacher)")


# Variable to see if we are generating from the filter or not
filter = 0

# Table to stock all the scores into
tableScores = 0

# Variable to read users permission to see what functions he/she can use (1 = Student, 2 = Teacher / Admin)
permission_level = 1


# Call display_results for permission level 1
def display_results_level1(event):
    global window_display_result, hex_color, canvas_score, btn, lbl_fil_entry_pseudo, lbl_fil_entry_end_date, fil_listed_exercises, fil_selected_exercise, add_listed_exercises, add_selected_exercises, filter, tableScores, incrementing_number, entry_date_hour, entry_date_hour_list, entry_time_list, entry_nbtries_list, entry_nbok_list, entry_student_list, entry_exercise_list, lbl_add_combobox_exercise, entry_add_student, entry_add_date, entry_add_time, entry_add_nbok, entry_add_nbtries, permission_level

    if filter == 0:
        tableScores = allScores()       # define tableScores with all the scores in the table "scores"
    incrementing_number = 0
    for line in tableScores:            # For every line of value in the database
        incrementing_number += 1        # Add 1 to the variable
    if filter == 1:
        if incrementing_number == 0:        # If there is no value in the score / filter
            tableScores = allScores()       # Give to it all the values
            incrementing_number += 1
            messagebox.showinfo("Info", "No value like inserted in filter")
    if incrementing_number != 0:        # If there is at least 1 value
        incrementing_number = 0         # Reset variable and keep on with the window creation

        window_display_result = tk.Toplevel()
        window_display_result.title("Résultats")
        window_display_result.geometry("1100x900")
        window_display_result.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), minsize=50, weight=1)
        window_display_result.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), minsize=50,
                                                weight=1)

        # Frame for the filter
        canvas_filter = tk.Canvas(window_display_result, width=2000, height=500)
        canvas_filter.grid(row=1, column=0, padx=5, pady=5, columnspan=8, rowspan=1)
        canvas_filter.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=100, weight=0)
        canvas_filter.grid_rowconfigure((0), minsize=0, weight=1)

        # Main frame creation (points frame)
        canvas_score = tk.Canvas(window_display_result, width=2000, height=500, bg="white")
        canvas_score.grid(row=3, column=0, padx=5, pady=5, columnspan=8, rowspan=11)
        canvas_score.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=0, weight=1)
        canvas_score.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), minsize=49, weight=0)

        # Frame for the total of results
        canvas_total = tk.Canvas(window_display_result, width=2000, height=500, bg="white")
        canvas_total.grid(row=15, column=0, padx=5, pady=5, columnspan=8, rowspan=2)
        canvas_total.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=0, weight=0)
        canvas_total.grid_rowconfigure((0, 1), minsize=0, weight=0)


        # Creation of canvas_filter_or_add filter section
        # Create a list with all the exercises in it
        fil_listed_exercises = ["GEO01", "INFO02", "INFO05"]
        fil_selected_exercise = tk.StringVar()
        #   Creation of all the labels, entries and combo boxes for the filter section
        lbl_fil_exercise = tk.Label(canvas_filter, text="Exercise", font=("Arial", 10), width=15)
        lbl_fil_exercise.grid(row=0, column=0, ipady=5, padx=0, pady=5)
        lbl_fil_combobox_exercise = ttk.Combobox(canvas_filter, textvariable=fil_selected_exercise, values=fil_listed_exercises, width=15)
        lbl_fil_combobox_exercise.grid(row=0, column=1, ipady=5, padx=0, pady=5)
        lbl_fil_end_date = tk.Label(canvas_filter, text="Date fin", font=("Arial", 10), width=15)
        lbl_fil_end_date.grid(row=0, column=2, ipady=5, padx=0, pady=5)
        lbl_fil_entry_end_date = tk.Entry(canvas_filter, width=15)
        lbl_fil_entry_end_date.grid(row=0, column=3, ipady=5, padx=0, pady=5)
        lbl_space = tk.Label(canvas_filter, text=" ", font=("Arial", 10), width=10, height=1)
        lbl_space.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        lbl_space = tk.Label(canvas_filter, text=" ", font=("Arial", 10), width=15, height=1)
        lbl_space.grid(row=0, column=5, ipady=5, padx=0, pady=5)
        btn_result = tk.Button(canvas_filter, text="Filtrer", command=filter_scores, width=10, height=1)
        btn_result.grid(row=0, column=8, pady=10, padx=10)


        # Creation of canvas_score score labels etc.
        #   Create the headers (title, student, date...)
        lbl_title = tk.Label(window_display_result, text="TRAINING : AFFICHAGE", font=("Arial", 15), height=1)
        lbl_title.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        lbl_titleTotal = tk.Label(window_display_result, text="Total", font=("Arial", 15), width=10, height=1)
        lbl_titleTotal.grid(row=14, column=4, ipady=5, padx=0, pady=5)
        lbl_student = tk.Label(canvas_score, text="Eleve", font=("Arial", 10), width=18, height=1)
        lbl_student.grid(row=0, column=0, ipady=5, padx=0, pady=5)
        lbl_date_hour = tk.Label(canvas_score, text="Date Heure", font=("Arial", 10), width=25, height=1)
        lbl_date_hour.grid(row=0, column=1, ipady=5, padx=0, pady=5)
        lbl_time = tk.Label(canvas_score, text="Temps", font=("Arial", 10), width=15, height=1)
        lbl_time.grid(row=0, column=2, ipady=5, padx=0, pady=5)
        lbl_exercise = tk.Label(canvas_score, text="Exercise", font=("Arial", 10), width=20, height=1)
        lbl_exercise.grid(row=0, column=3, ipady=5, padx=0, pady=5)
        lbl_nbok = tk.Label(canvas_score, text="nb OK", font=("Arial", 10), width=15, height=1)
        lbl_nbok.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        lbl_nbtotal = tk.Label(canvas_score, text="nb Total", font=("Arial", 10), width=15, height=1)
        lbl_nbtotal.grid(row=0, column=5, ipady=5, padx=0, pady=5)
        lbl_percentSuccess = tk.Label(canvas_score, text="% réussi", font=("Arial", 10), width=13, height=1)
        lbl_percentSuccess.grid(row=0, column=6, ipady=5, padx=0, pady=5)


        # Insert values in canvas_score
        incrementing_number = 0
        for line in tableScores:        # For every line of value, show its value in the window
            if incrementing_number != 10:       # If the incrementing number is not 10 yet (lines not 10 yet)
                if incrementing_number < 10:
                    # Search students name in this row
                    student_name = get_student_name_by_id(tableScores[incrementing_number][2])
                    # Search exercise name in this row
                    exercise_name = get_exercise_name_by_id(tableScores[incrementing_number][1])

                    # Create each line with its score
                    label_student = tk.Label(canvas_score, text=student_name[0], font=("Arial", 10), width=18, bg="white")
                    label_student.grid(row=incrementing_number + 1, column=0, ipady=5, padx=0, pady=5)

                    label_date_hour = tk.Label(canvas_score, text=tableScores[incrementing_number][3], font=("Arial", 10), width=25, bg="white")
                    label_date_hour.grid(row=incrementing_number + 1, column=1, ipady=5, padx=0, pady=5)

                    label_time = tk.Label(canvas_score, text=tableScores[incrementing_number][4], font=("Arial", 10), width=15, bg="white")
                    label_time.grid(row=incrementing_number + 1, column=2, ipady=5, padx=0, pady=5)

                    label_exercise = tk.Label(canvas_score, text=exercise_name[0], font=("Arial", 10), width=20, bg="white")
                    label_exercise.grid(row=incrementing_number + 1, column=3, ipady=5, padx=0, pady=5)

                    label_nbok = tk.Label(canvas_score, text=tableScores[incrementing_number][6], font=("Arial", 10), width=15, bg="white")
                    label_nbok.grid(row=incrementing_number + 1, column=4, ipady=5, padx=0, pady=5)

                    label_nbtotal = tk.Label(canvas_score, text=tableScores[incrementing_number][5], font=("Arial", 10), width=15, bg="white")
                    label_nbtotal.grid(row=incrementing_number + 1, column=5, ipady=5, padx=0, pady=5)

                    lbl_space = tk.Label(canvas_score, text=" ", font=("Arial", 10), width=5, height=1)
                    lbl_space.grid(row=0, column=7, ipady=5, padx=0, pady=5)


                # To prevent errors, we are going to check if the value is 0 (can't divide by 0)
                if tableScores[incrementing_number][5] == 0:
                    # Create a percentage bar
                    percentage_width = 90  # Adjust the width of the "bar"
                    percentage_height = 20  # Adjust the height of the "bar"
                    percentage_bar = tk.Canvas(canvas_score, width=percentage_width, height=percentage_height)
                    percentage_bar.grid(row=incrementing_number + 1, column=6, padx=0, pady=5)
                    filled_width = 5
                    percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="red")
                else:
                    # Calculate percentage of success
                    percentage_of_success = 100 / tableScores[incrementing_number][5]
                    percentage_of_success = percentage_of_success * tableScores[incrementing_number][6]
                    # Round the success percentage
                    percentage_of_success = round(percentage_of_success, 2)
                    # Create a percentage bar
                    percentage_width = 90              # Adjust the width of the "bar"
                    percentage_height = 20             # Adjust the height of the "bar"
                    percentage_bar = tk.Canvas(canvas_score, width=percentage_width, height=percentage_height)
                    percentage_bar.grid(row=incrementing_number + 1, column=6, padx=0, pady=5)
                    # Calculate the width for when we show the percentage
                    filled_width = percentage_width * (percentage_of_success / 100)
                    # Check for the percentage to see what color sticks better to it
                    if filled_width <= 25:
                        # If the player hasn't scored well once:
                        if percentage_of_success != 0:
                            percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="red")
                        else:
                            # Give to him 5% to show it better in the bar
                            filled_width = 5
                            percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="red")
                    elif percentage_of_success <= 65:
                        percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="yellow")
                    elif percentage_of_success <= 100:
                        percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="green")

            # Increment the number by 1
            incrementing_number = incrementing_number + 1

        # Création des label dans le canvas_total
        #   Show number of rows (column name)
        lbl_tot_nbrows = tk.Label(canvas_total, text="NbLignes", font=("Arial", 10), width=15)
        lbl_tot_nbrows.grid(row=0, column=0, ipady=5, padx=0, pady=5)
        #   Show total time (column name)
        lbl_tot_totalTime = tk.Label(canvas_total, text="Temps total", font=("Arial", 10), width=15)
        lbl_tot_totalTime.grid(row=0, column=1, ipady=5, padx=0, pady=5)
        #   Show total of successes (column name)
        lbl_tot_nbok = tk.Label(canvas_total, text="Nb OK", font=("Arial", 10), width=15)
        lbl_tot_nbok.grid(row=0, column=2, ipady=5, padx=0, pady=5)
        #   Show total of tries (column name)
        lbl_tot_nbtries = tk.Label(canvas_total, text="Nb Total", font=("Arial", 10), width=15)
        lbl_tot_nbtries.grid(row=0, column=3, ipady=5, padx=0, pady=5)
        #   Show % of total (column name)
        lbl_tot_percent = tk.Label(canvas_total, text="% Total", font=("Arial", 10), width=15)
        lbl_tot_percent.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        #   Spaces
        lbl_tot_space1 = tk.Label(canvas_total, text=" ", font=("Arial", 10), width=15)
        lbl_tot_space1.grid(row=0, column=5, ipady=5, padx=0, pady=5)
        lbl_tot_space2 = tk.Label(canvas_total, text=" ", font=("Arial", 10), width=15)
        lbl_tot_space2.grid(row=0, column=6, ipady=5, padx=0, pady=5)
        lbl_tot_space3 = tk.Label(canvas_total, text=" ", font=("Arial", 10), width=15)
        lbl_tot_space3.grid(row=0, column=7, ipady=5, padx=0, pady=5)


        # Results
        # Show number of rows
        lbl_nbrows = tk.Label(canvas_total, text=incrementing_number, font=("Arial", 10), width=15, bg="white")
        lbl_nbrows.grid(row=1, column=0, ipady=5, padx=0, pady=5)

        # Get total time
        incrementing_number = 0                     # Auto-increment number to go to the next values
        totaltime = timedelta(seconds=0)            # Variable to stock the gotten value and add the next value in it
        gotten_value = 0                            # Variable to stock the value in X row
        for line in tableScores:
            gotten_value = tableScores[incrementing_number][4]
            totaltime = totaltime + gotten_value
            incrementing_number += 1
        # Show total time
        lbl_totalTime = tk.Label(canvas_total, text=totaltime, font=("Arial", 10), width=15, bg="white")
        lbl_totalTime.grid(row=1, column=1, ipady=5, padx=0, pady=5)

        # Get total of successses
        incrementing_number = 0                     # Auto-increment number to go to the next values
        totalok = 0                                 # Variable to stock the gotten value and add the next value in it
        for line in tableScores:
            gotten_value = tableScores[incrementing_number][6]
            totalok = totalok + gotten_value
            incrementing_number += 1
        # Show total of successes
        lbl_nbok = tk.Label(canvas_total, text=totalok, font=("Arial", 10), width=15, bg="white")
        lbl_nbok.grid(row=1, column=2, ipady=5, padx=0, pady=5)

        # Get total of tries
        incrementing_number = 0                     # Auto-increment number to go to the next values
        totaltries = 0                              # Variable to stock the gotten value and add the next value in it
        for line in tableScores:
            gotten_value = tableScores[incrementing_number][5]
            totaltries = totaltries + gotten_value
            incrementing_number += 1
        # Show total of tries
        lbl_nbtries = tk.Label(canvas_total, text=totaltries, font=("Arial", 10), width=15, bg="white")
        lbl_nbtries.grid(row=1, column=3, ipady=5, padx=0, pady=5)

        if totaltries != 0:
            # Get total of tries in %
            percentSuccess = 100 / totaltries
            percentSuccess = percentSuccess * totalok
            percentSuccess = round(percentSuccess, 2)
        else:
            percentSuccess = 5
        # Show % of total
        lbl_percent = tk.Label(canvas_total, text=f"{percentSuccess}%", font=("Arial", 10), width=15, bg="white")
        lbl_percent.grid(row=1, column=4, ipady=5, padx=0, pady=5)

        # Variable to keep displaying this function for this session
        permission_level = 1

        # color définition
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa
        # main loop
        window_display_result.configure(bg=hex_color)
        window_display_result.mainloop()
    else:
        messagebox.showinfo("Info", "No score to display")


# Call display_results for permission level 2
def display_results_level2(event):
    global window_display_result, hex_color, canvas_score, btn, lbl_fil_entry_pseudo, lbl_fil_entry_end_date, fil_listed_exercises, fil_selected_exercise, add_listed_exercises, add_selected_exercises, filter, tableScores, incrementing_number, entry_date_hour, entry_date_hour_list, entry_time_list, entry_nbtries_list, entry_nbok_list, entry_student_list, entry_exercise_list, lbl_add_combobox_exercise, entry_add_student, entry_add_date, entry_add_time, entry_add_nbok, entry_add_nbtries, permission_level, entry_student, entry_exercise

    # List to get the specific value in specific entry later
    entry_date_hour_list = []
    entry_time_list = []
    entry_nbtries_list = []
    entry_nbok_list = []
    entry_student_list = []
    entry_exercise_list = []

    if filter == 0:
        tableScores = allScores()       # define tableScores with all the scores in the table "scores"
    incrementing_number = 0
    for line in tableScores:            # For every line of value in the database
        incrementing_number += 1        # Add 1 to the variable
    if filter == 1:
        if incrementing_number == 0:        # If there is no value in the score / filter
            tableScores = allScores()       # Give to it all the values
            incrementing_number += 1
            messagebox.showinfo("Info", "No value like inserted in filter")
    if incrementing_number != 0:        # If there is at least 1 value
        incrementing_number = 0         # Reset variable and keep on with the window creation

        window_display_result = tk.Toplevel()
        window_display_result.title("Résultats")
        window_display_result.geometry("1100x900")
        window_display_result.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9), minsize=50, weight=1)
        window_display_result.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16), minsize=50,
                                                weight=1)

        # Frame for the filter
        canvas_filter_or_add = tk.Canvas(window_display_result, width=2000, height=500)
        canvas_filter_or_add.grid(row=1, column=0, padx=5, pady=5, columnspan=8, rowspan=2)
        canvas_filter_or_add.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=100, weight=0)
        canvas_filter_or_add.grid_rowconfigure((0, 1, 2), minsize=0, weight=1)

        # Main frame creation (points frame)
        canvas_score = tk.Canvas(window_display_result, width=2000, height=500, bg="white")
        canvas_score.grid(row=3, column=0, padx=5, pady=5, columnspan=8, rowspan=11)
        canvas_score.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=0, weight=1)
        canvas_score.grid_rowconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), minsize=49, weight=0)

        # Frame for the total of results
        canvas_total = tk.Canvas(window_display_result, width=2000, height=500, bg="white")
        canvas_total.grid(row=15, column=0, padx=5, pady=5, columnspan=8, rowspan=2)
        canvas_total.columnconfigure((0, 1, 2, 3, 4, 5, 6, 7, 8), minsize=0, weight=0)
        canvas_total.grid_rowconfigure((0, 1), minsize=0, weight=0)


        # Creation of canvas_filter_or_add filter section
        # Create a list with all the exercises in it
        fil_listed_exercises = ["GEO01", "INFO02", "INFO05"]
        fil_selected_exercise = tk.StringVar()
        #   Creation of all the labels, entries and combo boxes for the filter section
        lbl_fil_pseudo = tk.Label(canvas_filter_or_add, text="Pseudo", font=("Arial", 10), width=18)
        lbl_fil_pseudo.grid(row=0, column=0, ipady=5, padx=0, pady=5)
        lbl_fil_entry_pseudo = tk.Entry(canvas_filter_or_add, width=18)
        lbl_fil_entry_pseudo.grid(row=0, column=1, ipady=5, padx=0, pady=5)
        lbl_fil_exercise = tk.Label(canvas_filter_or_add, text="Exercise", font=("Arial", 10), width=15)
        lbl_fil_exercise.grid(row=0, column=2, ipady=5, padx=0, pady=5)
        lbl_fil_combobox_exercise = ttk.Combobox(canvas_filter_or_add, textvariable=fil_selected_exercise, values=fil_listed_exercises, width=15)
        lbl_fil_combobox_exercise.grid(row=0, column=3, ipady=5, padx=0, pady=5)
        lbl_fil_end_date = tk.Label(canvas_filter_or_add, text="Date fin", font=("Arial", 10), width=15)
        lbl_fil_end_date.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        lbl_fil_entry_end_date = tk.Entry(canvas_filter_or_add, width=15)
        lbl_fil_entry_end_date.grid(row=0, column=5, ipady=5, padx=0, pady=5)
        btn_result = tk.Button(canvas_filter_or_add, text="Filtrer", command=filter_scores, width=10, height=1)
        btn_result.grid(row=0, column=7, pady=10, padx=10)


        # Creation of canvas_filter_or_add add section
        # Create a list with all the exercises in it
        add_listed_exercises = ["GEO01", "INFO02", "INFO05"]
        add_selected_exercise = tk.StringVar()
        #   Creation of all the labels and entries
        #       Labels
        lbl_add_student = tk.Label(canvas_filter_or_add, text="Ajouter éleve:", font=("Arial", 10), width=18)
        lbl_add_student.grid(row=1, column=0, ipady=5, padx=0, pady=5)
        lbl_add_date = tk.Label(canvas_filter_or_add, text="Date et Heure:", font=("Arial", 10), width=20)
        lbl_add_date.grid(row=1, column=1, ipady=5, padx=0, pady=5)
        lbl_add_time = tk.Label(canvas_filter_or_add, text="Temps:", font=("Arial", 10), width=10)
        lbl_add_time.grid(row=1, column=2, ipady=5, padx=0, pady=5)
        lbl_add_exercise = tk.Label(canvas_filter_or_add, text="Exercise:", font=("Arial", 10), width=10)
        lbl_add_exercise.grid(row=1, column=3, ipady=5, padx=0, pady=5)
        lbl_add_nbok = tk.Label(canvas_filter_or_add, text="Nbok:", font=("Arial", 10), width=10)
        lbl_add_nbok.grid(row=1, column=4, ipady=5, padx=0, pady=5)
        lbl_add_nbtries = tk.Label(canvas_filter_or_add, text="Nbtries:", font=("Arial", 10), width=10)
        lbl_add_nbtries.grid(row=1, column=5, ipady=5, padx=0, pady=5)
        #       Entries
        entry_add_student = tk.Entry(canvas_filter_or_add, font=("Arial", 10), width=15)
        entry_add_student.grid(row=2, column=0, ipady=5, padx=0, pady=5)
        entry_add_date = tk.Entry(canvas_filter_or_add, font=("Arial", 10), width=15)
        entry_add_date.grid(row=2, column=1, ipady=5, padx=0, pady=5)
        entry_add_time = tk.Entry(canvas_filter_or_add, font=("Arial", 10), width=15)
        entry_add_time.grid(row=2, column=2, ipady=5, padx=0, pady=5)
        lbl_add_combobox_exercise = ttk.Combobox(canvas_filter_or_add, textvariable=add_selected_exercise, values=add_listed_exercises, width=7)
        lbl_add_combobox_exercise.grid(row=2, column=3, ipady=5, padx=0, pady=5)
        entry_add_nbok = tk.Entry(canvas_filter_or_add, font=("Arial", 10), width=7)
        entry_add_nbok.grid(row=2, column=4, ipady=5, padx=0, pady=5)
        entry_add_nbtries = tk.Entry(canvas_filter_or_add, font=("Arial", 10), width=7)
        entry_add_nbtries.grid(row=2, column=5, ipady=5, padx=0, pady=5)
        btn_add = tk.Button(canvas_filter_or_add, text="Ajouter", command=add_score_from_filter, width=10, height=1)
        btn_add.grid(row=2, column=7, pady=10, padx=10)

        # Creation of canvas_score score labels etc.
        #   Create the headers (title, student, date...)
        lbl_title = tk.Label(window_display_result, text="TRAINING : AFFICHAGE", font=("Arial", 15), height=1)
        lbl_title.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        lbl_titleTotal = tk.Label(window_display_result, text="Total", font=("Arial", 15), width=10, height=1)
        lbl_titleTotal.grid(row=14, column=4, ipady=5, padx=0, pady=5)
        lbl_student = tk.Label(canvas_score, text="Eleve", font=("Arial", 10), width=18, height=1)
        lbl_student.grid(row=0, column=0, ipady=5, padx=0, pady=5)
        lbl_date_hour = tk.Label(canvas_score, text="Date Heure", font=("Arial", 10), width=20, height=1)
        lbl_date_hour.grid(row=0, column=1, ipady=5, padx=0, pady=5)
        lbl_time = tk.Label(canvas_score, text="Temps", font=("Arial", 10), width=10, height=1)
        lbl_time.grid(row=0, column=2, ipady=5, padx=0, pady=5)
        lbl_exercise = tk.Label(canvas_score, text="Exercise", font=("Arial", 10), width=10, height=1)
        lbl_exercise.grid(row=0, column=3, ipady=5, padx=0, pady=5)
        lbl_nbok = tk.Label(canvas_score, text="nb OK", font=("Arial", 10), width=10, height=1)
        lbl_nbok.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        lbl_nbtotal = tk.Label(canvas_score, text="nb Total", font=("Arial", 10), width=10, height=1)
        lbl_nbtotal.grid(row=0, column=5, ipady=5, padx=0, pady=5)
        lbl_percentSuccess = tk.Label(canvas_score, text="% réussi", font=("Arial", 10), width=13, height=1)
        lbl_percentSuccess.grid(row=0, column=6, ipady=5, padx=0, pady=5)


        # Insert values in canvas_score
        incrementing_number = 0
        for line in tableScores:        # For every line of value, show its value in the window
            if incrementing_number != 10:       # If the incrementing number is not 10 yet (lines not 10 yet)
                if incrementing_number < 10:
                    # Search students name in this row
                    student_name = get_student_name_by_id(tableScores[incrementing_number][2])
                    # Search exercise name in this row
                    exercise_name = get_exercise_name_by_id(tableScores[incrementing_number][1])
                    # Create each line with its score
                    entry_student = tk.Entry(canvas_score, font=("Arial", 10), width=18, bg="white")
                    entry_student.insert(0, student_name[0])
                    entry_student.grid(row=incrementing_number + 1, column=0, ipady=5, padx=0, pady=5)
                    # Save this entry in the list
                    entry_student_list.append(entry_student.get())

                    entry_date_hour = tk.Entry(canvas_score, font=("Arial", 10), width=20, bg="white")
                    entry_date_hour.insert(0, tableScores[incrementing_number][3])
                    entry_date_hour.grid(row=incrementing_number + 1, column=1, ipady=5, padx=0, pady=5)
                    # Save this entry in the list
                    entry_date_hour_list.append(entry_date_hour)

                    entry_time = tk.Entry(canvas_score, font=("Arial", 10), width=10, bg="white")
                    entry_time.insert(0, tableScores[incrementing_number][4])
                    entry_time.grid(row=incrementing_number + 1, column=2, ipady=5, padx=0, pady=5)
                    # Save this entry in the list
                    entry_time_list.append(entry_time)

                    entry_exercise = tk.Entry(canvas_score, font=("Arial", 10), width=10, bg="white")
                    entry_exercise.insert(0, exercise_name[0])
                    entry_exercise.grid(row=incrementing_number + 1, column=3, ipady=5, padx=0, pady=5)
                    # Save this entry in the list
                    entry_exercise_list.append(entry_exercise.get())

                    entry_nbok = tk.Entry(canvas_score, font=("Arial", 10), width=10, bg="white")
                    entry_nbok.insert(0, tableScores[incrementing_number][6])
                    entry_nbok.grid(row=incrementing_number + 1, column=4, ipady=5, padx=0, pady=5)
                    # Save this entry in the list
                    entry_nbok_list.append(entry_nbok)

                    entry_nbtotal = tk.Entry(canvas_score, font=("Arial", 10), width=10, bg="white")
                    entry_nbtotal.insert(0, tableScores[incrementing_number][5])
                    entry_nbtotal.grid(row=incrementing_number + 1, column=5, ipady=5, padx=0, pady=5)
                    # Save this entry in the list
                    entry_nbtries_list.append(entry_nbtotal)

                    lbl_space = tk.Label(canvas_score, text=" ", font=("Arial", 10), width=15, height=1)
                    lbl_space.grid(row=0, column=7, ipady=5, padx=0, pady=5)
                    lbl_space = tk.Label(canvas_score, text=" ", font=("Arial", 10), width=15, height=1)
                    lbl_space.grid(row=0, column=8, ipady=5, padx=0, pady=5)

                    btn_delete = tk.Button(canvas_score, text="Supprimer", command=lambda id=tableScores[incrementing_number][0]: delete_and_open_again(id), width=10, height=1)
                    btn_delete.grid(row=incrementing_number + 1, column=7, pady=10, padx=10)

                    btn_edit = tk.Button(canvas_score, text="Modifier", command=lambda score_id=tableScores[incrementing_number][0], window_row=incrementing_number: find_values_update(score_id, window_row), width=10, height=1)
                    btn_edit.grid(row=incrementing_number + 1, column=8, pady=10, padx=10)


                # To prevent errors, we are going to check if the value is 0 (can't divide by 0)
                if tableScores[incrementing_number][5] == 0:
                    # Create a percentage bar
                    percentage_width = 90  # Adjust the width of the "bar"
                    percentage_height = 20  # Adjust the height of the "bar"
                    percentage_bar = tk.Canvas(canvas_score, width=percentage_width, height=percentage_height)
                    percentage_bar.grid(row=incrementing_number + 1, column=6, padx=0, pady=5)
                    filled_width = 5
                    percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="red")
                else:
                    # Calculate percentage of success
                    percentage_of_success = 100 / tableScores[incrementing_number][5]
                    percentage_of_success = percentage_of_success * tableScores[incrementing_number][6]
                    # Round the success percentage
                    percentage_of_success = round(percentage_of_success, 2)
                    # Create a percentage bar
                    percentage_width = 90              # Adjust the width of the "bar"
                    percentage_height = 20             # Adjust the height of the "bar"
                    percentage_bar = tk.Canvas(canvas_score, width=percentage_width, height=percentage_height)
                    percentage_bar.grid(row=incrementing_number + 1, column=6, padx=0, pady=5)
                    # Calculate the width for when we show the percentage
                    filled_width = percentage_width * (percentage_of_success / 100)
                    # Check for the percentage to see what color sticks better to it
                    if filled_width <= 25:
                        # If the player hasn't scored well once:
                        if percentage_of_success != 0:
                            percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="red")
                        else:
                            # Give to him 5% to show it better in the bar
                            filled_width = 5
                            percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="red")
                    elif percentage_of_success <= 65:
                        percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="yellow")
                    elif percentage_of_success <= 100:
                        percentage_bar.create_rectangle(0, 0, filled_width, percentage_height, fill="green")

            # Increment the number by 1
            incrementing_number = incrementing_number + 1


        # Création des label dans le canvas_total
        #   Show number of rows (column name)
        lbl_tot_nbrows = tk.Label(canvas_total, text="NbLignes", font=("Arial", 10), width=15)
        lbl_tot_nbrows.grid(row=0, column=0, ipady=5, padx=0, pady=5)
        #   Show total time (column name)
        lbl_tot_totalTime = tk.Label(canvas_total, text="Temps total", font=("Arial", 10), width=15)
        lbl_tot_totalTime.grid(row=0, column=1, ipady=5, padx=0, pady=5)
        #   Show total of successes (column name)
        lbl_tot_nbok = tk.Label(canvas_total, text="Nb OK", font=("Arial", 10), width=15)
        lbl_tot_nbok.grid(row=0, column=2, ipady=5, padx=0, pady=5)
        #   Show total of tries (column name)
        lbl_tot_nbtries = tk.Label(canvas_total, text="Nb Total", font=("Arial", 10), width=15)
        lbl_tot_nbtries.grid(row=0, column=3, ipady=5, padx=0, pady=5)
        #   Show % of total (column name)
        lbl_tot_percent = tk.Label(canvas_total, text="% Total", font=("Arial", 10), width=15)
        lbl_tot_percent.grid(row=0, column=4, ipady=5, padx=0, pady=5)
        #   Spaces
        lbl_tot_space1 = tk.Label(canvas_total, text=" ", font=("Arial", 10), width=15)
        lbl_tot_space1.grid(row=0, column=5, ipady=5, padx=0, pady=5)
        lbl_tot_space2 = tk.Label(canvas_total, text=" ", font=("Arial", 10), width=15)
        lbl_tot_space2.grid(row=0, column=6, ipady=5, padx=0, pady=5)
        lbl_tot_space3 = tk.Label(canvas_total, text=" ", font=("Arial", 10), width=15)
        lbl_tot_space3.grid(row=0, column=7, ipady=5, padx=0, pady=5)


        # Results
        # Show number of rows
        lbl_nbrows = tk.Label(canvas_total, text=incrementing_number, font=("Arial", 10), width=15, bg="white")
        lbl_nbrows.grid(row=1, column=0, ipady=5, padx=0, pady=5)

        # Get total time
        incrementing_number = 0                     # Auto-increment number to go to the next values
        totaltime = timedelta(seconds=0)            # Variable to stock the gotten value and add the next value in it
        gotten_value = 0                            # Variable to stock the value in X row
        for line in tableScores:
            gotten_value = tableScores[incrementing_number][4]
            totaltime = totaltime + gotten_value
            incrementing_number += 1
        # Show total time
        lbl_totalTime = tk.Label(canvas_total, text=totaltime, font=("Arial", 10), width=15, bg="white")
        lbl_totalTime.grid(row=1, column=1, ipady=5, padx=0, pady=5)

        # Get total of successses
        incrementing_number = 0                     # Auto-increment number to go to the next values
        totalok = 0                                 # Variable to stock the gotten value and add the next value in it
        for line in tableScores:
            gotten_value = tableScores[incrementing_number][6]
            totalok = totalok + gotten_value
            incrementing_number += 1
        # Show total of successes
        lbl_nbok = tk.Label(canvas_total, text=totalok, font=("Arial", 10), width=15, bg="white")
        lbl_nbok.grid(row=1, column=2, ipady=5, padx=0, pady=5)

        # Get total of tries
        incrementing_number = 0                     # Auto-increment number to go to the next values
        totaltries = 0                                 # Variable to stock the gotten value and add the next value in it
        for line in tableScores:
            gotten_value = tableScores[incrementing_number][5]
            totaltries = totaltries + gotten_value
            incrementing_number += 1
        # Show total of tries
        lbl_nbtries = tk.Label(canvas_total, text=totaltries, font=("Arial", 10), width=15, bg="white")
        lbl_nbtries.grid(row=1, column=3, ipady=5, padx=0, pady=5)

        if totaltries != 0:
            # Get total of tries in %
            percentSuccess = 100 / totaltries
            percentSuccess = percentSuccess * totalok
            percentSuccess = round(percentSuccess, 2)
        else:
            percentSuccess = 5
        # Show % of total
        lbl_percent = tk.Label(canvas_total, text=f"{percentSuccess}%", font=("Arial", 10), width=15, bg="white")
        lbl_percent.grid(row=1, column=4, ipady=5, padx=0, pady=5)

        # Variable to keep displaying this function for this session
        permission_level = 2

        # color définition
        rgb_color = (139, 201, 194)
        hex_color = '#%02x%02x%02x' % rgb_color  # translation in hexa

        # main loop
        window_display_result.configure(bg=hex_color)
        window_display_result.mainloop()
    else:
        messagebox.showinfo("Info", "No score to display")


# Function to get all the values in the filters parameters and filter the scores
def filter_scores():
    global filter, tableScores, permission_level
    if permission_level == 2:
        pseudo = lbl_fil_entry_pseudo.get()
    else:
        # Get the values
        pseudo = users_pseudo()
        exercise = fil_selected_exercise.get()
        end_date = lbl_fil_entry_end_date.get()
    # If the pseudo has been inserted
    if pseudo:
        # Get the id
        pseudo_id = get_studentId(pseudo)
        # If there is no pseudo id
        if pseudo_id == None:
            messagebox.showinfo("Info", "player doesn't exist")
    # If no pseudo inserted in filter
    else:
        pseudo_id = '%'
    # If the exercise has been inserted
    if exercise:
        try:
            # Get the id
            exercise_id = get_exerciseId(exercise)
            # If there is no exercise id
            if exercise_id == None:
                messagebox.showinfo("Info", "Exercise doesn't exist")
        except ValueError:
            messagebox.showinfo("Info", "Exercise doesn't exist")
    else:
        exercise_id = '%'
    # If the end date has been inserted, keep going...
    if end_date:
        skip = 1
    # ...otherwise
    else:
        end_date = '%'
    # If nothing has been inserted
    if "%" in pseudo_id and "%" in exercise_id and "%" in end_date:
        # Set the filter variable to 0
        filter = 0
        # Close the window
        window_display_result.destroy()
        # Open the display window again using the permission level
        if permission_level == 2:
            display_results_level2(None)
        else:
            display_results_level1(None)
    # If there is anything in the filter
    else:
        try:
            # Filter with the gotten values
            tableScores = allScores_filter(pseudo_id[0], exercise_id[0], end_date)
            # Set the filter variable to 1
            filter = 1
            # Close the window
            window_display_result.destroy()
            # Open the display window again using the permission level
            if permission_level == 2:
                display_results_level2(None)
            else:
                display_results_level1(None)
        # If there is any error
        except ValueError:
            messagebox.showinfo("Info", "Error occured with the filter")


# FUnction to delete a value and display results again
def delete_and_open_again(id):
    delete_value(id)
    redisplay_results()

# Close window and display results again
def redisplay_results():
    global permission_level
    window_display_result.destroy()
    if permission_level == 2:
        display_results_level2(None)
    else:
        display_results_level1(None)

# Update the inserted values
def find_values_update(score_id, window_row):
    global tableScores
    row = get_score_row_value(score_id)
    # Fetch all values
    exercise_name = entry_exercise_list[window_row]
    if check_exercise(exercise_name) == None:  # If the name does not exist in the database
        messagebox.showinfo("Info", "The exercise doesn't exist. Values not updated")
    else:
        student_name = entry_student_list[window_row]
        student_id = get_studentId(student_name)
        exercise_id = get_exerciseId(exercise_name)
        finish_date = entry_date_hour_list[window_row].get()
        duration = entry_time_list[window_row].get()
        nb_tries = entry_nbtries_list[window_row].get()
        nb_ok = entry_nbok_list[window_row].get()
        try:
            # Define variable with the name to change the user to
            new_student_name = entry_student.get()
            # Update students name
            update_name(new_student_name, student_id[0])
            # Define variable with the name to change the user to
            new_exercise = entry_exercise.get()
            # Update the exercise
            print(exercise_name)
            print(new_exercise)
            print(exercise_id[0])
            update_exercise(new_exercise, exercise_id[0])
            # Update the row with the just saved values
            # update_score(exercise_id[0], student_id[0], finish_date, duration, nb_tries, nb_ok, score_id)
            messagebox.showinfo("Info", "Updated with success")
            redisplay_results()
        except ValueError:
            messagebox.showinfo("Info", "Error, verify data and retry.")


# Function to add a score from the add option (in the filter section)
def add_score_from_filter():
    exercise_name = lbl_add_combobox_exercise.get()
    if check_exercise(exercise_name) == None:  # If the name does not exist in the database
        messagebox.showinfo("Info", "The exercise doesn't exist. Values not updated")
    else:
        student_name = entry_add_student.get()
        if check_name(student_name) == None:  # If the name does not exist in the database
            student_name = student_name.capitalize()
            add_student(student_name)  # Add the student and the students score to the database
        student_id = get_studentId(student_name)
        exercise_id = get_exerciseId(exercise_name)
        finish_date = entry_add_date.get()
        duration = entry_add_time.get()
        nb_ok = entry_add_nbok.get()
        nb_tries = entry_add_nbtries.get()
        if nb_ok > nb_tries:
            messagebox.showinfo("Info", "Number of successes can't be bigger than the number of tries.")
        else:
            try:
                # Add score to the table "scores"
                add_score(exercise_id[0], student_id[0], finish_date, duration, nb_tries, nb_ok)
                messagebox.showinfo("Info", "Added with success")
                redisplay_results()
            except ValueError:
                messagebox.showinfo("Info", "Error. Verify data and retry.")





