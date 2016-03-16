
def palindrome(s):
    # edge cases
    if not s: return 0
    if len(s) == 1: return 1
    
    count = len(s)
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            count += 1
            j = 1
            while i - j - 1 >= 0 and i + j < len(s) and s[i - j - 1] == s[i + j]:
                count += 1; j += 1
    
    for i in range(1, len(s) - 1):
        if s[i - 1] == s[i + 1]:
            count += 1
            j = 1
            while i - j - 1 >= 0 and i + j + 1 < len(s) and s[i - j - 1] == s[i + j + 1]:
                count += 1; j += 1
    return count
    
def tripleArray(arr):
    if len(arr) < 3: return False
    if len(arr) == 3: return sorted(arr) == arr
    
    # dp
    dp = [1 for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return True if max(dp) >= 3 else False
    
def tripleArray2(arr):
    if len(arr) < 3: return False
    if len(arr) == 3: return sorted(arr) == arr
    
    # pointers
    min_1 = 2 **32 - 1; min_2 = 2 ** 32 - 1
    for i in range(1, len(arr)):
        if arr[i] < min_1:
            min_1 = arr[i]
        elif arr[i] < min_2:
            min_2 = arr[i]
        elif arr[i] > min_2:
            return True
    return False
    
def intersection(arr1, arr2):
    # sort & two pointers
    # hashtable
    
    def binarySearch(target, arr):
        left = 0; right = len(arr) - 1
        while left <= right:
            mid = (left + right) >> 1
            if arr[mid] == target: return mid
            elif arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return left
        
    if not arr1 or not arr2: return []
    
    arr1.sort(); arr2.sort()

    newStart = binarySearch(arr1[0], arr2)
    newEnd = binarySearch(arr1[-1], arr2)
    while newStart > 0 and arr2[newStart - 1] == arr2[newStart]: 
        newStart -= 1
    while newEnd < len(arr2) and arr2[newEnd + 1] == arr2[newEnd]:
        newEnd += 1
    arr2 = arr2[newStart : newEnd+1]
    ans = []
    i = 0; j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            ans.append(arr1[i])
            i += 1; j += 1
        elif arr1[i] < arr2[j]:
            i += 1
        else:
            j += 1
    return ans

def sameWay(arr):
    # make sure if arr[i] == arr[i - 1]
    if not arr or len(arr) == 1: return True
    if arr[-1] > arr[0]:
        i = 0
        while i < len(arr) - 1:
            if arr[i + 1] < arr[i]: return False
            i += 1
    elif arr[-1] < arr[0]:
        i = 0
        while i < len(arr) - 1:
            if arr[i + 1] > arr[i]: return False
            i += 1
    else:
        return True if len(set(arr)) == 1 else False 
    return True

def reverse(s):
    # make sure the upper and lower case
    # if 'Man bites dog' need to be changed to 'Dog bites man'
    if not s: return ''
    arr = s.split()
    if len(arr) == 1: return s
    return ' '.join(arr[::-1])

def findPath(matrix, x1, y1, x2, y2):
    # bfs
    # from point1 to point2
    
    def valid(i, j):
        if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1 or matrix[i][j] == 1 or visited[i][j]:
            return False
        return True
        
    if matrix[x1][y1] == 1 or matrix[x2][y2] == 1: return False
    node1 = [x1, y1]; node2 = [x2, y2]
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    queue = [node1]
    layer = 0
    while queue:
        newqueue = []
        while queue:
            node = queue.pop(0)
            x, y = node
            visited[x][y] = True
            if node == node2:
                return layer
            for i, j in zip([1, 0, -1, 0], [0, -1, 0, 1]):
                if valid(x + i, y + j):
                    newqueue.append([x + i, y + j])
        layer += 1
        queue = newqueue
    return -1


def findPath2(matrix, x1, y1, x2, y2):
    # bfs
    # from point1 to point2
    
    def valid(i, j):
        if i < 0 or i > len(matrix) - 1 or j < 0 or j > len(matrix[0]) - 1 or matrix[i][j] == 1 or visited[i][j]:
            return False
        return True
        
    if matrix[x1][y1] == 1 or matrix[x2][y2] == 1: return False
    node1 = [x1, y1]; node2 = [x2, y2]
    visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
    queue = [node1]
    layer = 0
    while queue:
        newqueue = []
        while queue:
            node = queue.pop(0)
            x, y = node
            visited[x][y] = True
            if node == node2:
                return layer
            for i, j in zip([1, 0, -1, 0], [0, -1, 0, 1]):
                if valid(x + i, y + j):
                    newqueue.append([x + i, y + j])
        layer += 1
        queue = newqueue
    return -1



        
def main():
    '''
    print(palindrome('aba'))
    print(palindrome('abba'))
    print(tripleArray2([2,2,2,2,4,1,3,3,6]))
    print(intersection([4,6,2,3,6], [2,3,6,6,9,12]))
    print(sameWay([2,4,3,43,6,6,8,8,4,6]))
    print(sameWay([3,3,3,2,1]))
    print(sameWay([2,3,3,3,2]))
    print(reverse('Man bites dog'))
    '''
    print(findPath([[0,0,0,1,1], [1,1,0,0,0], [0,0,0,0,1],[1,1,0,0,0]], 0, 0, 3, 4))
    
    print(findPath([[0,1,0,0,0,0,1,0,0,0], [0,0,0,1,0,1,0,1,0,0], [1,0,0,0,0,1,1,1,0,0],[0,0,1,1,1,1,0,1,0,0]], 0, 0, 3, 8))
main()