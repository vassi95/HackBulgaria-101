from print_info import *


def choice():
    print("""Enter the number of one of the following options(1 - 5):\n
    1. List all students with their GitHub accounts\n
    2. List all courses\n
    3. List all students and the courses he has been attending\n
    4. List the student that have attented the most courses\n
    5. Quit\n""")
    command = ""
    while command != "5":
        command = input("\nEnter command :")
        call_functions(command)


def call_functions(command):
    if command == "1":
        print(list_users())
    elif command == "2":
        print(list_courses())
    elif command == "3":
        print(list_s_and_c())
    elif command == "4":
        print(most_courses())
    elif command == "5":
        return
    else:
        print("Wrong command!")

if __name__ == '__main__':
    print(choice())

