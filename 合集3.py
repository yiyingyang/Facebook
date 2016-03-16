'''
1 longest common substring
2 zigzag change
3 (1-n) n+1 number, find duplicate
4 sort colors
5 subset


'''


def subset(arr):
    if not arr or len(arr) == 1: return [arr]
    
    # bit manipulation
    ans = []
    for i in range(2 ** (len(arr))):
        res = []
        count = i
        for j in range(len(arr)):
            bit = count & 1
            count >>= 1
            if bit:
                res.append(arr[j])
        if res not in ans:
            ans.append(res)
    return ans


def mutiplication(arr):
    if not arr or len(arr) == 1: return arr
    
    # bit manipulation
    # clarifying question: input duplicate? output sorted?
    
    ans = set()
    ranges = 2 ** len(arr)
    for i in range(ranges):
        count = i
        res = 1
        for j in range(len(arr)):
            bit = count & 1
            count >>= 1
            if bit:
                res *= arr[j]
        ans.add(res)
    return ans
    
    
def subarray(arr, target):
    
    for i in range(len(arr)):
        res = arr[i]
        for j in range(i+1, len(arr)):
            if res == target: return True
            res += target
    return False
    
    
    
def sortColors(arr):
    # edge cases
    if not arr or len(arr) == 0: return arr
    
    # two pointers
    p0 = 0; p2 = len(arr) - 1
    i = 0
    while i <= p2:
        if arr[i] == 0:
            arr[p0], arr[i] = arr[i], arr[p0]
            p0 += 1
        elif arr[i] == 2:
            arr[p2], arr[i] = arr[i], arr[p2]
            p2 -= 1
        i += 1
    return arr
    

def zigZagNumber(arr):
    # sort 
    new_arr = sorted(arr)
    size = len(arr)
    for i in range(1, size, 2) + range(0, size, 2):
        arr[i] = new_arr.pop()
    return arr
    
def zigZagNumber2(arr):
    # change the sequence
    if len(arr) == 0 or len(arr) == 1: return arr
    if len(arr) == 2: return sorted(arr)
    
    for i in range(len(arr) - 1):
        arr[i:i+2] = sorted(arr[i:i+2], reverse = i%2)
    return arr

def findDuplicate(arr):
    
    n = len(arr) - 1
    left = 1; right = n
    while left <= right:
        mid = (left + right) >> 1
        count = sum(i <= mid for i in arr)
        if count > mid:
            right = mid - 1
        else:
            left = mid + 1
    return left

def lcs(s,t):
    # edge case
    if not s or not t: return ''
    
    # dp
    dp = [[0 for _ in range(len(t) + 1)] for _ in range(len(s) + 1)]
    max_val, max_s = 0, ''
    for i in range(1, len(s)+1):
        for j in range(1, len(t)+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_val:
                    max_val, max_s = dp[i][j], s[i - dp[i][j] : i]
            else:
                dp[i][j] = 0
    
    return max_val, max_s

def main():
    print(sortColors([0,1,1,1,0,2,2,0,2,1]))
    print(zigZagNumber([1,9,3,4,5,11,6,7,14,8]))
    print(zigZagNumber2([1,9,3,4,5,11,6,7,14,8]))
    print(findDuplicate([1,2,3,4,5,5,6,7,8,9,10]))
    print(lcs('leetcode', 'codfish'))
    print(subset([1,2,2,3]))
    print(mutiplication([3, 5, 7]))
main()




    

