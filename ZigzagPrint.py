def zigzagPrint(arr):
    
    # edge cases
    if not arr: return ''
    if len(arr) == 1: return ','.join(map(str,arr[0][::-1]))
    m = len(arr); n = len(arr[0])
    ans = []
    
    # j - i = n-1 ~ 1-m
    for x in range(1 - m, n)[::-1]:
        for i in range(m):
            for j in range(n)[::-1]:
                if j == x + i:
                    ans.append(arr[i][j])
    return ','.join(map(str, ans))

def main():
    print(zigzagPrint([[1,2,3], [4,5,6]]))
    print(zigzagPrint([[1,2,3]]))
    print(zigzagPrint([[1], [4]]))
    print(zigzagPrint([[1,2,3,4], [5,6,7,8], [9,10,11,12]]))
    
    
main()
