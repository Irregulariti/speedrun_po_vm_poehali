from differce_equation import *

if __name__ == '__main__':
    s = input()
    alphabet = input().split()
    diff = DiffEquation(s,alphabet)
    print(diff.parse())
    polynom,char = diff.polynom()
    print(diff.substitution(polynom,char))
    print("")
