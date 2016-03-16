'''
balance("") -> ""
balance("(") -> ""
balance("()") -> "()"
balance(")(") -> ""
balance("(((((") -> ""
balance("(()()(") -> "()()"
balance(")(())(") -> "(())"
'''
def balance(s):
    # edge cases
    if not s or len(s) == 1 or len(set(s)) == 1: return ''
    
    # from left to right
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        elif s[i] == ')':
            if count:
                count -= 1
            else:
                s = s[:i] + '#' + s[i+1:]
    #print(s, count)
    if count:
        for i in reversed(range(len(s))):
            if not count: break
            if s[i] == '(':
                s = s[:i] + '#' + s[i+1:]
                count -= 1
    return s.replace('#', '')


def main():
    print(balance("()"))
    print(balance(")("))
    print(balance("((((("))
    print(balance("(()()("))
    print(balance(")(())("))
    print(balance(")(())("))
    print(balance("(())(()"))

main()