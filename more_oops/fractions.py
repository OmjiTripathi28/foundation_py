import math

class Fractions:
    def __init__(self, x, y):
        if y == 0:
            raise ValueError("Denominator cannot be zero")
        self.num = x
        self.den = y
        self._simplify()

    def _simplify(self):
        gcd = math.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd

    def __str__(self):
        return f"{self.num}/{self.den}"

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fractions(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fractions(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fractions(new_num, new_den)

    def __truediv__(self, other):
        if other.num == 0:
            raise ValueError("Cannot divide by zero")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fractions(new_num, new_den)


fr1 = Fractions(10,5)
fr2 = Fractions(12,6)

print(fr1)        
print(fr1 + fr2)  
print(fr1 - fr2)  
print(fr1 * fr2)  
print(fr1 / fr2)  
