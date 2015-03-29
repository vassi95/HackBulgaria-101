from datetime import date


def count_words(arr):
    counts = dict()
    for i in arr:
        counts[i] = counts.get(i, 0) + 1
    return counts

print (count_words(["apple", "banana", "apple", "pie"]))
print (count_words(["python", "python", "python", "ruby"]))


def unique_words_count(arr):
    counts = 0
    ar = []
    for i in arr:
        if i not in ar:
            ar.append(i)
            counts += 1

    return counts

print (unique_words_count(["apple", "banana", "apple", "pie"]))
print (unique_words_count(["python", "python", "python", "ruby"]))
print (unique_words_count(["HELLO!"] * 10))

def nan_expand(times):
    return "Not a " * times + "NaN"

print (nan_expand(0))
print (nan_expand(1))
print (nan_expand(2))
print (nan_expand(3))

def iterations_of_nan_expand(expanded):
    if expanded == "":
        return 0
    elif expanded.count('Not a') == 0:
        return False
    else:
        return expanded.count('Not a')
print (iterations_of_nan_expand(""))
print (iterations_of_nan_expand("Not a NaN"))
print (iterations_of_nan_expand(
'Not a Not a Not a Not a Not a Not a Not a Not a Not a Not a NaN'))
print (iterations_of_nan_expand("Show these people!"))

def prime_factorization(n):
    result = []
    number = n
    for divisor in range(2, n + 1):
        power = 0
        while number % divisor == 0:
            power += 1
            number //= divisor
        if power != 0:
            result.append((divisor, power))
    return result
print (prime_factorization(10))
print (prime_factorization(14))
print (prime_factorization(356))
print (prime_factorization(89))
print (prime_factorization(1000))

def same(items):
    index = 1
    result = [items[0]]
    while index < len(items) and items[index] == items[0]:
        result.append(items[index])
        index += 1
    return result

def group(lst):
    result = []
    while len(lst) != 0:

        result.append(same(lst))
        lst = lst[len(same(lst)):]
    return result
print (group([1, 1, 1, 2, 3, 1, 1]))



def max_consecutive(items):
    return max([len(item) for item in group(items)])
print (max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print (max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))


def groupby(func, seq):
    a = {}
    for i in seq:
        if func(i) in a:
            a[func(i)].append(i)
        else:
            a[func(i)] = [i]
    return a

print (groupby(lambda x: x % 2, [0, 1, 2, 3, 4, 5, 6]))
print (groupby(lambda x: 'odd' if x % 2 else 'even', [1, 2, 3, 5, 8, 9, 10]))
print (groupby(lambda x: x % 3, [0, 1, 2, 3, 4, 5, 6, 7]))
print (10 * '-')


def prepare_meal(number):
    a = number
    result = ""

    if number % 3 != 0 and number % 5 != 0:
        return result

    while a % 3 == 0:
        result += "spam"
        a /= 3
        if a % 3 == 0:
            result += " "

    if number % 5 == 0:
        if not number % 3 == 0:
            result += "eggs"
        else:
            result += " and eggs"
    return result

print (prepare_meal(5))
print (prepare_meal(3))
print (prepare_meal(27))
print (prepare_meal(15))
print (prepare_meal(45))
print (prepare_meal(7))


def reduce_file_path(path):
    result = []
    dirs = path.split('/')
    for directory in dirs:
        if directory == '' or directory == '.':
            pass
        elif directory == '..':
            if result != []:
                result.pop()
        else:
            result.append(directory)
    result1 = ""
    for directory in result:
        result1 += directory
        result1 += '/'
    result1 = result1[:-1]
    return '/' + result1

print (reduce_file_path("/"))
print (reduce_file_path("/srv/../"))
print (reduce_file_path("/srv/www/htdocs/wtf/"))
print (reduce_file_path("/srv/www/htdocs/wtf"))
print (reduce_file_path("/srv/./././././"))
print (reduce_file_path("/etc//wtf/"))
print(reduce_file_path("/etc/../etc/../etc/../"))
print (reduce_file_path("//////////////"))
print (reduce_file_path("/../"))


def is_an_bn(word):
    if word == "":
        return True
    if len(word) % 2 != 0:
        return False
    a = 0
    b = 0
    for i in range(0, len(word) // 2):
        if word[i] == 'a':
            a += 1
        else:
            return False
    for i in range(len(word) // 2, len(word)):
        if word[i] == 'b':
            b += 1
        else:
            return False
    return a == b

print (is_an_bn(""))
print (is_an_bn("rado"))
print (is_an_bn("aaabb"))
print (is_an_bn("aaabbb"))
print (is_an_bn("aabbaabb"))
print (is_an_bn("bbbaaa"))
print (is_an_bn("aaaaabbbbb"))



def is_credit_card_valid(number):
    lst = []
    number = str(number)
    for i in number:
        lst.append(int(i))
    digits = lst
    if len(digits) % 2 == False:
        return False
    new_list = []
    for i in range(0, len(digits)):
        if i % 2 == 0:
            new_list.append(digits[i])
        if i % 2 != 0:
            new_list.append(digits[i] + digits[i])
    if sum(new_list) % 10 == 0:
        return False
    else:
        return True

print (is_credit_card_valid(79927398713))
print (is_credit_card_valid(79927398715))



def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def goldbach(n):
    if n % 2 !=0 or n <= 2:
        return False

    result = [(x, n - x)
              for x in range(2, n // 2 + 1) if is_prime(x) and is_prime(n - x)]
    return result
print (goldbach(4))
print (goldbach(6))
print (goldbach(8))
print (goldbach(10))
print (goldbach(100))


def magic_square(matrix):
    size = len(matrix)
    summ = sum(matrix[0])
    for i in range(1, size):
        if sum(matrix[i]) != summ:
            return False
    for i in range(0, size):
        col_sum = 0
        for j in range(0, size):
            col_sum += matrix[j][i]
        if col_sum != summ:
            return False
    main_diag_sum = 0
    second_diag_sum = 0
    for i in range(0, size):
        main_diag_sum += matrix[i][i]
        second_diag_sum += matrix[i][size - i - 1]
    if main_diag_sum != summ or second_diag_sum != summ:
        return False
    return True

print (magic_square([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print (magic_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]))
print (magic_square([[7, 12, 1, 14], [2, 13, 8, 11],
[16, 3, 10, 5], [9, 6, 15, 4]]))
print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))


def leap_y(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

def friday_years(start, end):
    friday_y = 0
    for year in range(start, end + 1):
        fridays = leap_y(year)
        fromdate = date(year, 1, 1).weekday()
        todate = date(year, 1, 2).weekday()
        if fromdate == 4 or todate == 4 and fridays:
            friday_y += 1

    return friday_y

print(friday_years(1000, 2000))
print(friday_years(1753, 2000))
print(friday_years(1990, 2015))


