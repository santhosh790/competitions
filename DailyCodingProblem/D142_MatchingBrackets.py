'''
You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string.
Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
'''


def matchingParanthasis(exp):
    stack = []

    for each in exp:
        if each == '(':
            stack.append('(')
        elif each == ')':
            i = len(stack)-1
            flag = 0
            while i >= 0:
                if stack[i] == '*':
                    stack.pop()
                    flag = 1
                elif stack[i] == '(':
                    stack.pop()
                    flag = 1
                    break
                i -= 1
            if flag == 0:
                return False
        elif each == '*':
            stack.append('*')

    stCount = 0
    opCount = 0

    for each in stack:
        if each == '(':
            opCount += 1
        elif each == '*':
            stCount += 1

    return len(stack) == 0 or stCount >= opCount


print(matchingParanthasis("(*))*("))