import sqlite3


class Table:

    def __init__(self):
        pass

    def create(self):
        db = sqlite3.connect('Table.db')
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT,
                               monthly_salary INTEGER, yearly_bonus INTEGER, possition TEXT)
        ''')
        db.commit()

    def fill_in_table(self):
        conn = sqlite3.connect('Table.db')
        cursor = conn.cursor()
        employees = int(input("Enter the numbe of employees in the company: "))
        i = 0
        while i < employees:
            name = input("enter name:  ")
            ms = int(input("enter monthly_salary:  "))
            yb = int(input("enter yearly_bonus:  "))
            pos = input("enter possition:  ")
            cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES(?, ?, ?, ?)", (name, ms, yb, pos))
            i += 1
            conn.commit()

if __name__ == "__main__":
    b = Table()
    b.create()
