import sys
import os
from random import randint


def cat():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
        my_file = open(filename, "r")
        result = my_file.read()
        my_file.close()
        return result

if __name__ == '__main__':
    print(cat())


def cat2():
    result = ""
    for i in range(1, len(sys.argv)):
        filename = sys.argv[i]
        readFile = open(filename, "r")
        result += readFile.read() + '\n'
        readFile.close()
    return result

if __name__ == '__main__':
    print(cat2())


def generate_numbers():
    filename = sys.argv[1]
    numbers_count = int(sys.argv[2])
    file = open(filename, "w+")
    for i in range(numbers_count):
        number = str(randint(1, 1000))
        file.write(number + '')
    file.close()

if __name__ == '__main__':
    print(generate_numbers())


def sum_numbers():
    summ = 0
    filename = sys.argv[1]
    file = open(filename, "r")
    numbers = file.read().split(" ")
    numbers = list(numbers)
    for number in numbers:
        number = int(number)
        summ += number
    return summ
    file.close()

if __name__ == '__main__':
    print(sum_numbers())


def duhs():
    path = sys.argv[1]
    size = 0
    for (path, dirs, files) in os.walk(path):
        for file in files:
            filename = os.path.join(path, file)
            size += os.path.getsize(filename)
    return size

if __name__ == '__main__':
    print(duhs())
