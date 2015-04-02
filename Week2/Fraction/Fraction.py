class Fraction:

    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __add__(self, other):
        sum_numer = self.numer * other.denom + self.denom * other.numer
        sum_denom = self.denom * other.denom
        return (sum_numer // sum_denom)

    def __sub__(self, other):
        sub_numer = self.numer * other.denom - self.denom * other.numer
        sub_denom = self.denom * other.denom
        return (sub_numer // sub_denom)

    def __eq__(self, other):
        return self.numer / self.denom == other.numer / other.denom

    def __str__(self):
        return "{} / {}".format(self.numer, self.denom)

    def __repr__(self):
        return self.__str__()

    def __mul__(self, other):
        numerator = self.numer * other.numer
        denominator = self.denom * other.denom

        for i in range(1, 11)[::-1]:
            if denominator % i == 0 and numerator % i == 0:
                numerator //= i
                denominator //= i
        return (str(numerator) + "/" + str(denominator))

a = Fraction(1, 2)
b = Fraction(2, 4)
print(a == b)
print(a + b)
print(a - b)
print(a * b)
