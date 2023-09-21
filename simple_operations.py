import re

def remove_brackets(s: str, alphabet: list):
    stack = []
    j = 0
    first = ""
    print(s)
    while s[j] != "(":
        first += s[j]
        j += 1
    if first == "":
        first = 1
    operands = ('+', '-', '^')
    k = ""
    dict = {}
    ok = True
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
            ok = False
        elif s[i] == ')':
            if len(stack) == 1:
                dict[k] = s[stack[0]:i + 1]
                stack.pop(-1)
                ok = True
                k = ''
            else:
                stack.pop(-1)
        if (s[i] in operands or i == 0) and ok:
            k = s[i]
            print(k)
        elif ok:
            k += s[i]

    print(dict)
    ans = ""
    for (mn,sk) in dict.items():
        s.replace(mn,"")
        s.replace(sk,"")
        sk = sk[1:len(sk)-1]
        if "(" in sk:
            sk = remove_brackets(sk, alphabet)
        sk1 = []
        for i in range()
        sk = re.split(r"[+-]", sk)
        for el in sk:
            if el == '1':
                ans += "+" + mn
            post = '+' + mn + el
            if el.isdigit() and mn.isdigit():
                post = int(el)*int(mn)
                if post >=0:
                    post = str(post)
                else:
                    post = str(post)

            elif el.isdigit():
                post = '+'+el + mn
            ans += post
    if ans[0]=='+':
        ans = ans[1:]
    return ans
