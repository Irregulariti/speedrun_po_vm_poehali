from differce_equation import *

if __name__ == '__main__':
    s = input()
    alphabet = input().split()
    diff = DiffEquation(s,alphabet)
    print(diff.parse())
    print(diff.substitution())
    print("")
