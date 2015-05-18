import sqlite3
from create_db import Make_tables
from insert_into import *


def list_users():
    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    cursor.execute("SELECT id, name, github FROM students")
    u = cursor.fetchall()
    all_students = []
    for i in u:
        student = "{} - {} - {}".format(i[0], i[1], i[2])
        all_students.append(student)
    all_students = "\n".join(all_students)
    return all_students


def list_courses():
    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM courses")
    c = cursor.fetchall()
    all_courses = []
    for i in c:
        course = "{} - {}".format(i[0], i[1])
        all_courses.append(course)
    all_courses = "\n".join(all_courses)
    return all_courses


def list_s_and_c():
    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    request = """SELECT students.name,
        courses.name
        FROM courses JOIN students
        ON courses.id IN (
        SELECT course_id
        FROM s_and_c
        WHERE student_id = students.id)"""
    result = cursor.execute(request)
    st_co = []
    for i in result:
        sc = "{} - {}".format(i[0], i[1])
        st_co.append(sc)
    st_co = "\n".join(st_co)
    return st_co


def most_courses():
    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    request = """SELECT students.name, COUNT(s_and_c.student_id)
        FROM students JOIN s_and_c
        ON students.id = student_id
        WHERE students.id IN (
        SELECT student_id
        FROM s_and_c
        GROUP BY student_id
        ORDER BY COUNT(*) DESC
        LIMIT 1)"""
    cursor.execute(request)
    c = cursor.fetchall()
    most_courses = []
    for i in c:
        course = "{} - {}".format(i[0], i[1])
        most_courses.append(course)
    most_courses = "\n".join(most_courses)
    return most_courses
if __name__ == '__main__':
    print(list_users())
    print("\n\n")
    print(list_courses())
    print("\n\n")
    print(list_s_and_c())
    print("\n\n")
    print(most_courses())
