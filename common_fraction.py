import math


class CF:
    num: int
    den: int

    def __init__(self, num, den):
        num = num
        den = den


def general(a: CF, b: CF):
    return math.lcm(a.den, b.den)


def sumCF(a: CF, b: CF):
    gener = general(a, b)
    return CF(a.num * gener // a.den + b.num * gener // b.den, gener)


def multi(a: CF, b: CF):
    return reduce(CF(a.num * b.num, a.den * b.den))


def divide(a: CF, b: CF):
    k = CF(b.den, b.num)
    return multi(a, k)


def reduce(a: CF):
    gcd = math.gcd(a.num, a.den)
    if gcd != 1:
        a.num = a.num // gcd
        a.den = a.den // gcd
    return a
