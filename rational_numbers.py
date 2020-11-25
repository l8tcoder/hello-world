from __future__ import division
import math

class Rational:
    def __init__(self, numer, denom):
        self.numer = int(numer)
        self.denom = int(denom)

        if self.denom == 0:
            raise ValueError("Divisor cannot be zero")
        elif self.denom < 0:
            self.denom = 0 - self.denom
            self.numer = 0 - self.numer

        self.numer = self.numer / self.my_gcd(numer, denom)
        self.denom = self.denom / self.my_gcd(numer, denom)

    def my_abs(self, x):
        if int(x) < 0:
            return 0 - int(x) 
        else:
            return int(x)

    def my_gcd(self, num, den):
        gcd = None
        smaller = None
        larger = None

        if int(num) == 0:
            return int(den)

        # figure out which is larger

        if self.my_abs(num) > self.my_abs(den):
            smaller = den
            larger = num
        else:
            smaller = num
            larger = den

        # calculate gcd

        for i in range(self.my_abs(smaller)):
            if smaller % (i + 1) == 0 and larger % (i + 1) == 0:
                gcd = i + 1 

        return gcd

    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        n = self.numer * other.denom + other.numer * self.denom
        d = self.denom * other.denom
        return Rational(n, d)

    def __sub__(self, other):
        n = self.numer * other.denom - other.numer * self.denom
        d = self.denom * other.denom 
        return Rational(n / self.my_gcd(n, d), d / self.my_gcd(n, d))

    def __mul__(self, other):
        n = self.numer * other.numer
        d = self.denom * other.denom
        return Rational(n / self.my_gcd(n, d), d / self.my_gcd(n, d))

    def __truediv__(self, other):
        n = self.numer * other.denom
        d = self.denom * other.numer
        return Rational(n, d) 

    def __abs__(self):
        return Rational(self.my_abs(self.numer), self.my_abs(self.denom))

    def __pow__(self, power):
        if power >= 0:
            return Rational(self.numer ** power, self.denom ** power)
        else:
            return Rational(self.denom ** self.my_abs(power), self.numer ** self.my_abs(power))

    def __rpow__(self, base):
        return (base ** self.numer) ** (1 / self.denom)
