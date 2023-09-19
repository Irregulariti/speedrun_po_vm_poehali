from common_fraction import *


class DiffEquation:
    equation: str
    alphabet: list
    order: int

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

        cft = []
        for string in temp:
            c = 0
            if '+' in string:
                c = int(string[string.find("+") + 1:])
            cft.append(c)
        self.order = max(cft) - min(cft)

        construct = ""
        s = self.order
        for i in range(0,s+1):
            if i == 0:
                construct += 'h^(' + str(s-i) + ')'
                continue
            kf = kft[i]
            if kf >= 0:
                kf = '+' + str(kf)
            else:
                kf = str(kf)
            if s-i == 0:
                construct += kf
                continue
            construct += kf+'*h^(' + str(s-i) + ')'
        construct += "=n+1"
        print(construct)
