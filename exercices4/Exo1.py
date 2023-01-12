from Liste import Liste
from random import randint

def pgcd(a, b):

    if b == 0:
        return a
    else:
        r=a%b
        return pgcd(b, r)

class Fraction:
    def __init__(self, num:int, denom:int):
        if(denom <= 0):
            raise ValueError

        self.num = num
        self.denom = denom

        self._irreductible()

    def __str__(self):
        if(self.denom > 1):
            return str(self.num) + "/" + str(self.denom)
        return str(self.num)

    def __eq__(self, fraction):
        return self.num * fraction.denom == self.denom * fraction.num

    def __lt__(self, fraction):
        return self.num * fraction.denom < self.denom * fraction.num

    def __add__(self, fraction):
        return Fraction(
            self.num * fraction.denom + fraction.num * self.denom,
            self.denom * fraction.denom
        )

    def __mul__(self, fraction):
        return Fraction(
            self.num * fraction.num,
            self.denom * fraction.denom
        )

    def _irreductible(self):

        a = pgcd(self.num, self.denom)

        self.num /= a
        self.denom /= a

class Debut:
    def __init__(self):
        liste = Liste()

        for i in range(10):
            f = Fraction(randint(1, 50), randint(1, 50))
            liste.ajoute(f)

        print(liste)

Debut()