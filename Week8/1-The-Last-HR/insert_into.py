import sqlite3
from create_db import Make_tables
from make_request import GetInformation


def insert_into_courses(self, courses):
    db = sqlite3.connect('info.db')
    sql = "INSERT INTO courses (name) VALUES (?)"
    cursor = db.cursor()
    cursor.executemany(sql, (courses, ))
    db.commit()


def insert_into_students(self, students):
    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    cursor.executemany('''INSERT INTO students(name, github) \
        VALUES(?, ?)''', (students, ))
    db.commit()


def insert_into_new(self, s_and_c):
    db = sqlite3.connect('info.db')
    cursor = db.cursor()
    info = []
    for sc in s_and_c:
        student_id = s_and_c[0]
        courses = s_and_c[1]
        for c in courses:
            cursor.execute("""SELECT FROM courses \
                WHERE name = ? """, (c, ))
            course_id = self.cursor.fetchone()
            info.append((student_id, course_id[0]))
    cursor.executemany("""INSERT INTO s_and_c(student_id, course_id) \
        VALUES(?, ?)""", (info, ))
    db.commit()

if __name__ == '__main__':
    b = Make_tables()
    a = GetInformation()
    b.create_tables()
    insert_into_courses(a.make_requests())
    insert_into_students(a.make_requests())
    insert_into_new(a.make_requests())
