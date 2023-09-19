def remove_brackets(s: str, alphabet: list):
    stack = []
    j = 0
    first = ""
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
                dict[k] = s[stack[0]:i+1]
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
