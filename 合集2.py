'''
15 f(n) = f(n-1) + 2*f(n-3).   
    Follow up:  f(n, k) = f(n - 1) + 2 * f(n - k)
    if(n <=0) f(n) = 1
22 Converting a BST to circular Doubly linked list - no extra space. 把左右指针当成 pre ， next 指针

16 n th Fibonacci number mod 10
    %5 %20 [1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0]
    %2 %3  [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0]
    array

decode ways all possibility
'A' -> 1
'B' -> 2
...
'Z' -> 26
            if 0 < x < 10: dp[i] = dp[i-1]
            elif x == 10 or x == 20: dp[i] = dp[i-2]
            elif 10 < x < 20 or 20 < x <= 26: dp[i] = dp[i-1]+dp[i-2]
            elif x > 26 and s[i]!= '0':
                dp[i] = dp[i-1]
            else: return 0
    
minimum window substring, 求string s里面最短的含有string t的window  - 'ABCDSCBSDBC' - 'SBC' - 'SDBC'
    - followup: 输入是一个字符串和一个集合。。集合就是我们要的之后最小窗口里面必须有的字符 - 'ABCDSCBSDBC' - 'SBC' - 'SCB'

sorted Integer array，输出sorted array consisted of squares of input integers，比如[1,3,5] -> [1,9,25]会有负数， 感觉是一道典型的tw pointers。。。或者可以设一个输出数组，指针两端向中间移动，每次把较大值放到数组中，从后往前放，代码更简洁。。。

找两个字符串中长度为N以上的共同子串。。LZ脑抽没答好。。。其实遍历一下就行

Given a string list，find all pairs of strings which can be combined to be a palindrome. eg: cigar + tragic -> cigartragic, none + xenon -> nonexenon。如果有n个词，每个词长度m，用HashSet可以用O(nm^2)做出来

task scheduling
    input: ABAABB
    cooldown: 2 (don't repeat characters in this unit of time)
    output: AB_AB_AB
    Followup: could change sequence
    
Find first k common elements in n sorted arrays - hashmap - merge sort 

Give the count and the number following in the series. for   e.g 1122344 first line output : 21221324 next line : 12112211121214 and so on...

给一个board，上面有0 和1，1不可以走，0 可以走。任意给一个start一个end，让输出最短的步数。follow up输出路径
    follow up: 但是每次都是可以纵向两步横向一步，或者横向一步纵向两部，问步数和路径。

判断一个树是不是另一个树的子树

15 f(n) = f(n-1) + 2*f(n-3).   
    Follow up:  f(n, k) = f(n - 1) + 2 * f(n - k)
    if(n <=0) f(n) = 1
'''    
        
def magicNumberDP(n):
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        if n - 3 <= 0:
            dp[i] = dp[i-1] + 2
        else:
            dp[i] = dp[i-1] + 2 * dp[i - 3]
    return dp[-1]
    
def magicNumberDPSpace(n):
    dp = [1 for _ in range(3)]
    dp[0] = 1; dp[1] = 3; dp[2] = 5
    for _ in range((n-1)/3):
        dp[0] = dp[2] + 2 * dp[0]
        dp[1] = dp[0] + 2 * dp[1]
        dp[2] = dp[1] + 2 * dp[2]
    return dp[(n-1) % 3]
    
def magicNumber2Space(n, k):
    dp = [1 for _ in range(k)]
    for i in range(1, k):
        dp[i] = dp[i - 1] + 2
    for _ in range((n-1) / k):
        for i in range(k):
            dp[i] = dp[i - 1] + 2 * dp[i]
    return dp[(n-1) % k]

def magicNumber2(n, k):
    dp = [1 for _ in range(n)]
    for i in range(1, n):
        if n - k <= 0:
            dp[i] = dp[i-1] + 2
        else:
            dp[i] = dp[i-1] + 2 * dp[i - k]
    return dp[-1]

def findKCommonHash(arrays, k):
    # hashmap
    import collections
    n = len(arrays)
    maxLen = len(max(arrays, key = len))
    count = collections.defaultdict(int)
    i = 0
    while i < maxLen:
        for x in range(n):
            if i < len(arrays[x]):
                count[arrays[x][i]] += 1
                if count[arrays[x][i]] == k:
                    return arrays[x][i]
        i += 1
    return None
    
def findKCommonHashAll(arrays, k):
    # hashmap
    import collections
    n = len(arrays)
    maxLen = len(max(arrays, key = len))
    count = collections.defaultdict(int)
    for x in range(n):
        for i in range(len(arrays[x])):
            count[arrays[x][i]] += 1
    for key in sorted(count):
        if count[key] >= k: return key
    return None


def findKCommonHeap(arrays, k):
    # merge sort
    import heapq, collections
    n = len(arrays)
    heap = []; count = collections.defaultdict(int)
    for i in range(n):
        heap.append((arrays[i][0], i, 0))
    heapq.heapify(heap)
    while heap:
        val, x, index = heapq.heappop(heap)
        count[val] += 1
        if count[val] == k: return val
        if index < len(arrays[x]) - 1:
            heapq.heappush(heap, (arrays[x][index+1], x, index + 1))
    return None

def squareSorted(arr):
    
    # O(nlogn)
    arr.sort(key = lambda x: abs(x))
    return [i * i for i in arr]


def squarePointer(arr):
    
    # two pointers O(n)
    
    ans = []
    left = 0; right = len(arr) - 1
    while left <= right:
        if abs(arr[left]) >= abs(arr[right]):
            ans.insert(0, arr[left] ** 2)
            left += 1
        else:
            ans.insert(0, arr[right] ** 2)
            right -= 1
    return ans
    
def fibModten(n):
    '''
    %5 %20 [1,1,2,3,0,3,3,1,4,0,4,4,3,2,0,2,2,4,1,0]
    %2 %3  [1,1,0,1,1,0,1,1,0,1,1,0,1,1,0,1,1,0]
    '''
    # 60
    k = n % 60
    
    dp = [1 for _ in range(60)]
    for i in range(2, 60):
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10
    return dp[k - 1]

def taskScheduling():
    pass

def taskSchedulingRandom():
    pass

def countingNumber(s, k):
    
    s = str(s)
    for _ in range(k):
        news = ''
        char = None; count = 0
        for i in range(len(s)):
            if not char:
                char = s[i]; count = 1
            elif char == s[i]:
                count += 1
            elif char != s[i]:
                news += str(count) + char
                char = s[i]; count = 1
        news += str(count) + char
        s = news;
        print(s)
        

def main():
    print(magicNumberDP(14))
    print(magicNumberDPSpace(14))
    print(magicNumber2(100, 9))
    print(magicNumber2Space(100, 9))
    #print(findKCommonHashAll([[2,3,5], [2,3], [1,4], [1,5]], 2))
    #print(findKCommonHeap([[2,3,5], [2,3], [1,4], [1,5]], 2))
    #print(findKCommonHash([[2,3,5], [2,3], [1,4], [1,5]], 2))
    #print(findKCommonHash([[1,3,4,5,9,11],[1,2,7,8,9], [2,3,4,5,6,7,9], [1,3,4,5,7, 9]], 4))
    #print(squareSorted([-5,-3,-1,0, 1, 2, 4, 5, 6]))
    #print(squarePointer([-5,-3,-1,0, 1, 2, 4, 5, 6]))
    #print(fibModten(600))
    #print(countingNumber(1122344, 10))


main()


