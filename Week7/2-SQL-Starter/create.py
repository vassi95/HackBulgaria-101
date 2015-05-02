import sqlite3


class Table:

    def create(self):
        db = sqlite3.connect('Table.db')
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT,
                               monthly_salary INTEGER, yearly_bonus INTEGER, possition TEXT)
        ''')
        cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES('Ivan Ivanov', 5000, 10000, 'Software Developer')")
        cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES('Rado Rado', 500, 0, 'Technical Support Intern')")
        cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES('Ivo Ivo', 10000, 100000, 'CEO')")
        cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES('Petar Petrov', 3000, 1000, 'Marketing Manager')")
        cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES('Maria Georgieva', 8000, 10000, 'COO')")
        db.commit()

if __name__ == "__main__":
    b = Table()
    b.create()
