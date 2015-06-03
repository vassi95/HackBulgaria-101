import sql_manager
import re


class PasswordError(Exception):
    pass


def main_menu():
    print("Welcome to our bank service. You are not logged in. \nPlease register or login")

    while True:
        command = input("$$$>")

        if command == 'register':
            username = input("Enter your username: ")
            password = valid_password()

            sql_manager.register(username, password)

            print("Registration Successfull")

        elif command == 'login':
            username = input("Enter your username: ")
            password = (input("Enter your password: "))
            logged_user = sql_manager.login(username, password)
            if logged_user:
                logged_menu(logged_user)
            else:
                print("Login failed")

        elif command == 'help':
            print("login - for logging in!")
            print("register - for creating new account!")
            print("exit - for closing program!")

        elif command == 'exit':
            return
        else:
            print("Not a valid command")


def logged_menu(logged_user):
    print("Welcome you are logged in as: " + logged_user.get_username())
    while True:
        command = input("Logged>>")

        if command == 'info':
            print("You are: " + logged_user.get_username())
            print("Your id is: " + str(logged_user.get_id()))
            print("Your balance is:" + str(logged_user.get_balance()) + '$')

        elif command == 'changepass':
            new_pass = input("Enter your new password: ")
            sql_manager.change_pass(new_pass, logged_user)

        elif command == 'change-message':
            new_message = input("Enter your new message: ")
            sql_manager.change_message(new_message, logged_user)

        elif command == 'show-message':
            print(logged_user.get_message())

        elif command == 'help':
            print("info - for showing account info")
            print("changepass - for changing passowrd")
            print("change-message - for changing users message")
            print("show-message - for showing users message")


def valid_password():
    password = input("Enter your password: ")
    length = len(password)
    if length < 8:
        raise PasswordError("Enter longer password(at least 8 symbols)")
    if not re.search('[a-zA-Z]', password):
        raise PasswordError("Your password must contain both upper and lower case")
    if not re.search('[0-9]', password):
        raise PasswordError("Your password must contain digits")
    if not re.search('[^a-zA-Z0-9]', password):
        raise PasswordError("Your password must contain special symbols")
    ugly_regx = r"(?=^.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])"
    if not re.match(ugly_regx, password):
        password = input("Invalid password\nEnter password: ")
    else:
        return password


def main():
    sql_manager.create_clients_table()
    main_menu()

if __name__ == '__main__':
    main()

