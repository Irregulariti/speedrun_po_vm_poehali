from common_fraction import *
from quadratic_equation import QuadEquation
from simple_operations import remove_brackets

class DiffEquation:
    equation: str
    alphabet: list
    order: int
    char_root1: int
    char_root2: int
    kft: list
    cft: list

    def __init__(self, equation: str, alphabet: list):
        self.equation = equation
        self.alphabet = alphabet

    def parse(self):
        diff = 'Z'

        eq = self.equation  # Z[n+2] -9Z[n+1] + 14Z[n] = n + 1
        a = self.alphabet  # ['n']

        temp = []
        start_index = -1
        kft = []
        k = ""

        for i in range(len(eq)):
            if eq[i] == "Z":
                if k == '': k = 1
                kft.append(int(k))
                k = ""
            else:
                k += eq[i]

            if eq[i] == '[':
                start_index = i
            elif eq[i] == ']':
                temp.append(eq[start_index + 1:i])
                k = ""

        self.kft = kft
        cft = []

        for string in temp:
            c = 0
            if '+' in string:
                c = int(string[string.find("+") + 1:])
            cft.append(c)

        self.cft = cft
        self.order = max(cft) - min(cft)

        construct = ""
        s = self.order
        for i in range(0, s + 1):
            if i == 0:
                construct += 'h^(' + str(s - i) + ')'
                continue
            kf = kft[i]
            if kf >= 0:
                kf = '+' + str(kf)
            else:
                kf = str(kf)
            if s - i == 0:
                construct += kf
                continue
            construct += kf + 'h^(' + str(s - i) + ')'
        construct += "=0"

        if s == 2:
            self.char_root1, self.char_root2 = QuadEquation(construct, kft).solve()
        return construct

    def polynom(self):
        temp = self.equation[self.equation.find('=') + 1:]
        s = list()
        operands = ('+', '-', '^', "(", ")")
        for i in range(len(temp)):
            if not temp[i].isdigit() and temp[i] not in operands:
                s.append(temp[i])
        char = s[0]
        polynom = ""
        ind = 65
        for i in range(len(temp)):
            if temp[i] == char:
                polynom += chr(ind) + char + '+'  # only for 1 degree
                ind += 1
            if i == len(temp) - 1:
                if temp[i - 1] != char:
                    polynom += chr(ind)
                ind += 1
        return polynom, char

    def substitution(self, polynom, char):
        eq = self.equation
        kft = self.kft
        cft = self.cft
        done = ""
        for i in range(len(cft)):
            k = str(kft[i])
            if int(k) >= 0:
                k = '+' + k
            prefix = polynom.replace(char, "(" + char + "+" + str(cft[i]) + ")")
            if cft[i] == 0:
                prefix = polynom
            if int(k)==1 and i == 0:
                done+= prefix
                continue
            done += k + '(' + prefix + ")"
        remove_brackets(done,self.alphabet)
        return done


