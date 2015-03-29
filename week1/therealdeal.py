def sum_of_divisors(n):
    summ = 0
    for i in range(1, n + 1):
        if n % i == 0:
            summ += i
    return summ

print (sum_of_divisors(8))
print (sum_of_divisors(1000))


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

print(is_prime(8))
print(is_prime(11))


def prime_number_of_divisors(n):
    numm = 0
    for i in range(1, n + 1):
        if n % i == 0:
            numm += i
    if is_prime(numm):
        return True
    return False

print (prime_number_of_divisors(8))
print (prime_number_of_divisors(9))


def contains_digit(number, digit):
    num = list(str(number))
    if str(digit) in num:
        return True
    return False

print (contains_digit(1000, 0))
print (contains_digit(12346789, 5))


def contains_digits(number, digits):
    for num in digits:
        if contains_digit(number, num) == False:
            return False
    return True

print (contains_digits(402123, [0, 3, 4]))
print (contains_digits(666, [6, 4]))


def is_number_balanced(n):
    sum1 = 0
    sum2 = 0
    length = len(str(n))
    if length == 1:
        return True
    if length % 2 == 0:
        for i in str(n)[0:length // 2]:
            sum1 += int(i)
        for i in str(n)[length // 2:length]:
            sum2 += int(i)
    else:
        for i in str(n)[0:length // 2]:
            sum1 += int(i)
        for i in str(n)[length // 2 + 1:length]:
            sum2 += int(i)
    return sum1 == sum2

print (is_number_balanced(13))
print (is_number_balanced(121))
print (is_number_balanced(4518))
print (is_number_balanced(28471))


def count_substrings(haystack, needle):
    a = haystack.count(needle)
    return a


print (count_substrings("This is a test string", "is"))
print (count_substrings("babababa", "baba"))
print (count_substrings("We have nothing in common!", "really?"))


def zero_insert(n):
    result = []
    n = str(n)
    for i in range(0, len(n) - 1):
        if n[i] == n[i+1] or (int(n[i]) + int(n[i+1])) % 10 == 0:
            result.append(n[i] + '0')
        else:
            result.append(n[i])
    result.append(n[len(n) - 1])
    number = ""
    for i in result:
        number += str(i)
    return int(number)
print (zero_insert(55555))
print(zero_insert(116457))
print(zero_insert(6446))


def sum_matrix(matr):
    summ = 0
    for row in matr:
        for elem in row:
            summ += elem
    return summ

m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))


def damage(x, y, matrix):
    damage = 0
    a = len(matrix)
    b = len(matrix[0])
    bomb = matrix[x][y]
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                if 0 <= x + i < a and 0 <= y + j < b:
                    if bomb < matrix[x + i][y + j]:
                        damage += bomb
                    else:
                        damage += matrix[x + i][y + j]
    return damage


def matrix_bombing_plan(m):
    plan = {}
    total = sum_matrix(m)
    for x in range(len(m)):
        for y in range(len(m[x])):
            position = x, y
            plan[position] = total - damage(x, y, m)
    return plan

print (matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
