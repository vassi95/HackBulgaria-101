import sqlite3
from create import Table


class Employees:

    def list_employees(self):
        conn = sqlite3.connect("Table.db")
        cursor = conn.cursor()
        result = cursor.execute("SELECT id, name, monthly_salary, yearly_bonus, possition FROM users")
        for i in result:
            print("{} | {} | {} | {} | {}".format(i[0], i[1], i[2], i[3], i[4]))

    def monthly_spending(self):
        count = 0
        conn = sqlite3.connect("Table.db")
        cursor = conn.cursor()
        result = cursor.execute("SELECT monthly_salary FROM users")
        for row in result:
            count += int(''.join(map(str, row)))
        print("This company is spending $%d every month!" % count)

    def yearly_spending(self):
        conn = sqlite3.connect("Table.db")
        cursor = conn.cursor()
        cursor.execute("SELECT sum(yearly_bonus) + sum(monthly_salary)*12 FROM users")
        result = cursor.fetchone()
        print("This company is spending $%d every year!" % result)

    def add_employee(self):
        conn = sqlite3.connect('Table.db')
        cursor = conn.cursor()
        name = input("enter name:  ")
        ms = int(input("enter monthly_salary:  "))
        yb = int(input("enter yearly_bonus:  "))
        pos = input("enter possition:  ")
        cursor.execute("INSERT INTO users(name, monthly_salary, yearly_bonus, possition) VALUES(?, ?, ?, ?)", (name, ms, yb, pos))
        conn.commit()

    def delete_employee(self, number):
        conn = sqlite3.connect('Table.db')
        cursor = conn.cursor()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", number)
        conn.commit()

    def update_employee(self, number):
        conn = sqlite3.connect('Table.db')
        cursor = conn.cursor()
        name = input("enter name:  ")
        ms = int(input("enter monthly_salary:  "))
        yb = int(input("enter yearly_bonus:  "))
        pos = input("enter possition:  ")
        cursor.execute("UPDATE users SET name = ?, monthly_salary = ?, yearly_bonus = ?, possition = ? WHERE id = ?", (name, ms, yb, pos, number))
        conn.commit()

if __name__ == '__main__':
    a = Employees()
    b = Table()
    b.create()
    b.fill_in_table()
    a.list_employees()
    print('\n')
    a.monthly_spending()
    a.yearly_spending()
    print('\nAdd new employee! \n')
    a.add_employee()
    print('\n')
    a.list_employees()
    print('\n')
    a.delete_employee('6')
    print('Employee successfully deleted!\n')
    a.list_employees()
    print('\nUpdate employee !\n')
    a.update_employee('1')
    print('\n')
    a.list_employees()
