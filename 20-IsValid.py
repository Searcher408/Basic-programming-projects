class Solution:
    def isValid(self, s: str) -> bool:
        stk = list()

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stk.append(c)
            else:
                if stk:
                    if c == ')' and stk[-1] == '(':
                        stk.pop()
                    elif c == '}' and stk[-1] == '{':
                        stk.pop()
                    elif c == ']' and stk[-1] == '[':
                        stk.pop()
                    else:
                        return False
                else:
                    return False
        if stk:
            return False
        else:
            return True

class Solution:
    def isValid(self, s):
        while '{}' in s or '()' in s or '[]' in s:
            s = s.replace('{}', '')
            s = s.replace('[]', '')
            s = s.replace('()', '')
        return s == ''