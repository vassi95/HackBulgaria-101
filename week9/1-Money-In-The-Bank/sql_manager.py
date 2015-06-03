import sqlite3
from Client import Client_bank
from settings import DB_NAME, SQL_FILE
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()


def create_clients_table():
    with open(SQL_FILE, "r") as f:
        cursor.executescript(f.read())
    conn.commit()


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = ? WHERE id = ?"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    update_sql = "UPDATE clients SET password = ? WHERE id = ?"
    cursor.execute(update_sql, (new_pass, logged_user.get_id()))
    conn.commit()


def register(username, password):
    insert_sql = "insert into clients (username, password) values (?, ?)"
    cursor.execute(insert_sql, (username, password))
    conn.commit()


def login(username, password):
    select_query = "SELECT id, username, balance, message FROM clients \
    WHERE username = ? AND password = ? LIMIT 1"
    cursor.execute(select_query, (username, password))
    user = cursor.fetchone()

    if(user):
        return Client_bank(user[0], user[1], user[2], user[3])
    else:
        return False


def get_email(self, username):
    get_email = "SELECT email FROM clients WHERE username = ? LIMIT 1"
    cursor.execute(get_email, (username, ))
    user = cursor.fetchone()
    if user:
        return user[0]
    return False


def deposit(money, user):
    cursor.execute("""
    SELECT balance FROM clients WHERE username = ?
    """, (user,))
    balance = cursor.fetchone()
    total = balance[0] + money
    cursor.execute("""
    UPDATE clients SET balance = ? WHERE username = ?
    """, (total, user))
    conn.commit()


def withdraw(money, user):
    cursor.execute("""
    SELECT balance FROM clients WHERE username = ?
    """, (user,))
    balance = cursor.fetchone()
    total = balance[0]
    if total < money:
        print("There are not enough money to withdraw")
    elif total == money:
        cursor.execute("""
        UPDATE clients SET balance = ? WHERE username = ?
        """, (0, user))
        conn.commit()
    else:
        cursor.execute("""
        UPDATE clients SET balance = ? WHERE username = ?
        """, (total - money, user))
        conn.commit()


def display(user):
    cursor.execute("""
    SELECT balance FROM clients WHERE username = ?
    """, (user,))
    balance = cursor.fetchone()[0]
    return balance

