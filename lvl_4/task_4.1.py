# Задача 4.1.
# Домашнее задание на SQL

# В базе данных teacher создайте таблицу Students

# Структура таблицы: Student_Id - Integer, Student_Name - Text, School_Id - Integer (Primary key)

# Наполните таблицу следующими данными:

# 201, Иван, 1
# 202, Петр, 2
# 203, Анастасия, 3
# 204, Игорь, 4

# Напишите программу, с помощью которой по ID студента можно получать информацию о школе и студенте.

# Формат вывода:

# ID Студента:
# Имя студента:
# ID школы:
# Название школы:

import sqlite3

conn_to_db = sqlite3.connect('teacher.db')
cursor = conn_to_db.cursor()
query_create_tab_sc = """
CREATE TABLE School (
    School_Id INTEGER PRIMARY KEY ,
    School_Name TEXT NOT NULL ,
    Place_Count INTEGER NOT NULL);"""
query_create_tab_st = """
CREATE TABLE Students (
    Student_Id INTEGER PRIMARY KEY ,
    Student_Name TEXT,
    School_Id INTEGER NOT NULL);"""

