import sqlite3


class Make_tables:

    def __init__(self):
        self.db = sqlite3.connect('info.db')
        self.cursor = self.db.cursor()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY,
                name TEXT, github TEXT)
            ''')
        self.db.commit()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS courses (id INTEGER PRIMARY KEY,
                name TEXT)
            """)
        self.db.commit()
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS s_and_c(
                student_id INTEGER ,
                course_id INTEGER,
                PRIMARY KEY(student_id, course_id),
                FOREIGN KEY(student_id) REFERENCES students(id),
                FOREIGN KEY(course_id) REFERENCES courses(id))
            ''')
        self.db.commit()
