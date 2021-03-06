def addExpression(s, target):
    def dfs(start, end, last, curr, res):
        if start == end:
            if last == target:
                ans.append(res)
            return 
        for i in range(start + 1, end + 1):
            if start == 0:
                dfs(i, end, last + int(s[start:i]), int(s[start:i]), s[start:i])
            elif i == start + 1 or i != start + 1 and s[start] != '0':
                dfs(i, end, last + int(s[start:i]), int(s[start:i]), res + '+' + s[start:i])
                dfs(i, end, last - int(s[start:i]), int(s[start:i]), res + '-' + s[start:i])
                
    
    if len(s) == 0: return []
    if len(s) == 1: return [s] if int(s) == target else []
    
    ans = []
    dfs(0, len(s), 0, 0, '')
    return ans

def main():
    print(addExpression('1234560789', 100))
main()