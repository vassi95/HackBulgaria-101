def factorial(n):
    factorial = 1
    if n > 0:
        for i in range(1, n + 1):
            factorial *= i
    return factorial

print(factorial(0))
print(factorial(1))
print(factorial(5))


def fibonacci(n):
    fib = []
    a = 1
    b = 1
    fib.append(a)
    fib.append(b)
    for i in range(int(n - 2)):
        c = a + b
        fib.append(c)
        a = b
        b = c
    return fib
print (fibonacci(10))


def sum_of_digits(n):
    sum = 0
    while n:
        if n > 0:
            sum += n % 10
            n //= 10
        else:
            n = abs(n)
            sum += n % 10
            n //= 10
    return sum
print(sum_of_digits(1325132435356))


def fact_digits(n):
    summ = 0
    n = list(str(n))
    for i in n:
        summ += factorial(int(i))
    return summ
print(fact_digits(999))


def palindrome(obj):
    str(obj)
    p = obj[::-1]
    if p == obj:
        return True
    return False
print(palindrome("kapak"))
print(palindrome("baba"))


def to_digits(n):
    lst = []
    n = str(n)
    for i in n:
        lst.append(int(i))
    return lst
print(to_digits(123023))


def to_number(digits):
    number = ""
    for i in digits:
        number += str(i)
    return int(number)

print(to_number([1, 2, 3, 0, 2, 3]))


def fib_number(n):
    concat = ""
    a = 1
    b = 1
    concat += str(a) + str(b)
    for i in range(int(n - 2)):
        c = a + b
        concat += str(c)
        a = b
        b = c
    return concat
print(fib_number(10))
print(fib_number(3))


def count_vowels(str):
    count = 0
    for i in str:
        if i.lower() in "ayeoui":
            count += 1
    return count
print(count_vowels("A nice day to code!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))


def count_consonants(str):
    count = 0
    for i in str:
        if i.lower() in "bcdfghjklmnpqrstvwxz":
            count += 1
    return count
print(count_consonants("A nice day to code!"))
print(count_consonants("Theistareykjarbunga"))


def char_histogram(string):
    dict = {}
    c = 0
    for letter in string:
        c = string.count(letter)
        dict[letter] = c
    return dict
print(char_histogram("AAAAaaa!!!"))


def p_score(n):
    n = str(n)
    p = n[::-1]
    if p == n:
        return 1
    s = int(n) + int(str(n)[::-1])
    return 1 + p_score(s)
print(p_score(198))


def is_increasing(seq):
    if all(x < y for x, y in zip(seq, seq[1:])):
        return True
    else:
        return False
print(is_increasing([1, 2, 3, 4, 5]))
print(is_increasing([5, 6, -10]))


def is_decreasing(seq):
    if all(x > y for x, y in zip(seq, seq[1:])):
        return True
    else:
        return False
print(is_decreasing([1, 2, 3, 4, 5]))
print(is_decreasing([5, 4, -10]))


def is_hack(n):
    binary = bin(n)[2:]
    if n % 2 != 0:
        ones = binary.count("1")
    if str(binary) == str(binary[::-1]) and ones % 2 != 0:
        return True


def next_hack(n):
    next_number = n + 1
    while not is_hack(next_number):
        next_number = next_number + 1
    if is_hack(next_number):
        return next_number

print (next_hack(0))
print (next_hack(10))
