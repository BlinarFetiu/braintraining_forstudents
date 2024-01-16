"""
Author: Blinar Fetiu
File: database.py (connect to the database and create functions)
Module: ProjDBPY
Date: 02.01.2023
"""

import csv
import mysql.connector
import hashlib

# Example from here :
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# or here https://www.w3schools.com/python/python_mysql_getstarted.asp



# Function to open the connection with the database (buffered=True : Esegue senza chiedere ad ogni riga. autocommit=True : Esegue il salvataggio)
def open_dbconnection():
    global db_connection
    db_connection = mysql.connector.connect(host='127.0.0.1', port='3306',
                                   user='oikin', password='Pa$$w0rd', database='braintraining_forstudents',
                                   buffered=True, autocommit=True)
    

# Function to close the connection with the database
def close_dbconnection():
    db_connection.close()

open_dbconnection()


# Function to add the students to the Database
def add_student(pseudo, password):
    query = "INSERT INTO students (name, password, permission_level) values (%s, %s, 1)"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, password))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



# Function to get exercises ID
def get_exerciseId(exercise_name):
    query = "SELECT id FROM exercises WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercise_name,))
    row = cursor.fetchone()
    cursor.close()
    return row



# Function to get students ID
def get_studentId(student_name):
    query = "SELECT id FROM students WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (student_name,))
    row = cursor.fetchone()
    cursor.close()
    return row



# Function to add the students to the Database
def add_score(exercise_id, student_id, finish_date, duration, nb_tries, nb_successes):
    query = "INSERT INTO scores (Exercise_id, Student_id, finish_date, duration, nb_tries, nb_successes) values (%s, %s, %s, %s, %s, %s)"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercise_id, student_id, finish_date, duration, nb_tries, nb_successes,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



# Function to get students name by the ID
def get_student_name_by_id(student_id):
    query = "SELECT name FROM students WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (student_id,))
    row = cursor.fetchone()
    cursor.close()
    return row



# Function to get exercises name by the ID
def get_exercise_name_by_id(exercises_id):
    query = "SELECT name FROM exercises WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercises_id,))
    row = cursor.fetchone()
    cursor.close()
    return row



# Function to get all scores (then, we will insert 1 by 1 in the display window)
def allScores():
    query = "SELECT * FROM scores"
    cursor = db_connection.cursor()
    cursor.execute(query, multi=True)
    rows = cursor.fetchall()
    cursor.close()
    return rows



# Function to get all scores (according to the filter settings)
def allScores_filter(student_id, exercise_id, end_date):
    query = "SELECT * FROM scores WHERE student_id LIKE %s AND exercise_id LIKE %s AND finish_date LIKE %s;"
    cursor = db_connection.cursor()
    cursor.execute(query, (student_id, exercise_id, end_date,))
    rows = cursor.fetchall()
    cursor.close()
    return rows



# Function to test all gotten values from the "Scores" table (to test, just call the function)
def displayResultsTest():
    rownumber = 0
    print("eleve - date - temp - exercice - nbok - nbessais - % réussit")
    tableScores = allScores()
    for (row) in tableScores:
        exercise_name = get_exercise_name_by_id(tableScores[rownumber][1])
        student_name = get_student_name_by_id(tableScores[rownumber][2])
        # Print student from the score table
        print(f"{student_name[0]}", end=" - ")
        # Print finishing date from the score table
        print(f"{tableScores[rownumber][3]}", end=" - ")
        # Print time (duration) from the score table
        print(f"{tableScores[rownumber][4]}", end=" - ")
        # Print exercise from the score table
        print(f"{exercise_name[0]}", end=" - ")
        # Print number of successes from the score table
        print(f"{tableScores[rownumber][6]}", end=" - ")
        # Print number of tries from the score table
        print(f"{tableScores[rownumber][5]}", end=" - ")
        # Print % of successes from the score table
        print("%")
        # Add one to get to the next line
        rownumber = rownumber + 1



def delete_value(row_id):
    query = "DELETE FROM scores WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (row_id,))
    cursor.close()
    return None



# Check if players name already exists in table
def check_name(pseudo):
    query = "SELECT * FROM students WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (pseudo, ))
    row = cursor.fetchone()
    cursor.close()
    return row



# Check if exercises name exists in table
def check_exercise(exercise_name):
    query = "SELECT * FROM exercises WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercise_name, ))
    row = cursor.fetchone()
    cursor.close()
    return row



# Function to add the students to the Database
def update_score(exercise_id, student_id, finish_date, duration, nb_tries, nb_successes_, score_id):
    query = "UPDATE scores SET Exercise_id = %s, Student_id = %s, finish_date = %s, duration = %s, nb_tries = %s, nb_successes = %s WHERE id = %s;"
    cursor = db_connection.cursor()
    cursor.execute(query, (exercise_id, student_id, finish_date, duration, nb_tries, nb_successes_, score_id,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



# Function to update the users name
def update_name(username, id):
    query = "UPDATE students SET name = %s WHERE id = %s;"
    cursor = db_connection.cursor()
    cursor.execute(query, (username, id,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



# Function to update the exercise
def update_exercise(name, id):
    query = "UPDATE exercises SET name = %s WHERE id = %s;"
    cursor = db_connection.cursor()
    cursor.execute(query, (name, id,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



# Function to update the permission level
def update_permission(level, id):
    query = "UPDATE students SET permission_level = %s WHERE id = %s;"
    cursor = db_connection.cursor()
    cursor.execute(query, (level, id,))
    inserted_id = cursor.lastrowid
    cursor.close()
    return inserted_id



# Get all values in this row (of score)
def get_score_row_value(score_id):
    query = "SELECT * FROM scores WHERE id = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (score_id,))
    rows = cursor.fetchall()
    cursor.close()
    return rows


# Vertify the password
def verify_password(username, input_password):
    cursor = db_connection.cursor()
    query = "SELECT password FROM students WHERE name = %s"
    values = (username,)

    try:
        cursor.execute(query, values)
        result = cursor.fetchone()

        if result:
            stored_password = result[0]
            input_password_hash = hashlib.sha256(input_password.encode()).hexdigest()

            return input_password_hash == stored_password
        else:
            return False

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return False
    finally:
        cursor.close()


# Function to get users permission level
def get_users_level(student_name):
    query = "SELECT permission_level FROM students WHERE name = %s"
    cursor = db_connection.cursor()
    cursor.execute(query, (student_name,))
    row = cursor.fetchone()
    cursor.close()
    return row


