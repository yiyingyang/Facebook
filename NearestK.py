'''
decode ways
dfs
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
给一个array of points (x, y coordinates) , 然后给一个点origin, print k closest emelents to origin(heap - nlogn), follow up是如果array length很大 k很小(quick select - klogn),  问了time 和 space complexity
'''
# BUG POINT! Initiate heap as list and then heap = list(set(heap))
# 否则输出会把同一个距离算两遍

import collections, heapq, math
def nearestK(arr, origin, k):
    # edge cases
    if not arr: return []
    if len(arr) == 1: return arr[0]
    
    # get all the distances as a table
    table = collections.defaultdict(list)
    heap = []
    for x, y in arr:
        distance = math.sqrt(float( (x - origin[0]) ** 2 + (y - origin[1]) ** 2))
        table[distance].append([x, y])
        heap.append(distance)
    
    # use a heap
    heap = list(set(heap))
    heapq.heapify(heap)
    ans = []
    count = 0
    while count < k:
        i = heapq.heappop(heap)
        for pair in table[i]:
            ans.append(pair)
            count += 1
    return ans
    
import collections, math, random
def nearestK2(arr, origin, k):
    # edge cases
    if not arr: return []
    if len(arr) == 1: return arr[0]
    
    # get all the distances as a table
    table = collections.defaultdict(list)
    heap = set()
    for x, y in arr:
        distance = math.sqrt(float((x - origin[0]) ** 2 + (y - origin[1]) ** 2))
        table[distance].append([x, y])
        heap.add(distance)
    
    # quick select
    def quickSelect(arr,k):
        # edge case
        if len(arr) == 1 and k == 1: return arr[0]

        pivot = random.choice(arr)
        arr1 = []; arr2 = []
        for i in arr:
            if i < pivot: arr1.append(i)
            elif i > pivot: arr2.append(i)
        if len(arr1) >= k:
            return quickSelect(arr1, k)
        elif len(arr) - len(arr2) < k:
            return quickSelect(arr2, k - (len(arr) - len(arr2)))
        return pivot
        
    count = 0; i = 1
    ans = []
    while count < k:
        key = quickSelect(list(heap), i)
        for pair in table[key]:
            ans.append(pair)
            count += 1
        i += 1
    return ans

def test():
    def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        # dfs
        def valid(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or visited[i][j] or grid[i][j] != '1':
                return False
            return True
            
        def dfs(i, j):
            if not valid(i, j): return
            count += 1
            visited[i][j] = True
            for x, y in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                dfs(i + x, j + y)

        if not grid: return 0
        
        ans = []
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == '1':
                    count = 0
                    dfs(i, j)
                    ans.append(count)
        return max(ans)
    print(numIslands(["11000", "11000", "00100",  "00011"]))
        
def main():
    arr = [[1,4], [4,5], [5.6, 8.9], [2.5, 5.6]]
    origin = [1,4]
    print(nearestK2(arr, origin, 2))
    print(nearestK(arr, origin, 2))
    test()
    
main()


import sys
x = sys