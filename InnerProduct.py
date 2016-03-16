'''a
1. {2, 2, 2, 1, 5, 6, 6, ,7, ,7} -> {2,1,5,6,7,x,x,x,x,,x}

2. Inner product for sparse arrays
'''


def move(arr):
    if not arr or len(arr) == 1: return arr
    # prev, j as boundary
    prev = None;  j = 0
    for i in range(len(arr)):
        if not prev: 
            prev = arr[i]
            j += 1
        else:
            if arr[i] != prev:
                prev = arr[i]
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
    return arr
    
def innerProduct(arr1, arr2):
    
    # edge cases
    if not arr1 or not arr2: return 0
    if len(arr1) > len(arr2): return innerProduct(arr2, arr1)
    
    # one hashtable
    table = {}
    for i in range(len(arr1)):
        if arr1[i] != 0:
            table[i] = arr1[i]
    ans = 0
    for index, number in table.items():
        if arr2[index] != 0:
            ans += arr2[index] * number
    return ans


def innerProduct2(arr1, arr2):
    
    if not arr1 or not arr2: return 0
    if len(arr1) > len(arr2): return innerProduct(arr2, arr1)
    # pivot
    i = 0; ans = 0
    while i < len(arr1):
        if arr1[i] == 0: i += 1
        elif arr2[i] == 0: i += 1
        else: ans += arr1[i] * arr2[i]
    return ans
    


def main():
    arr = [2, 2, 2, 1, 5, 6, 6, 7, 7]
    arr = [2, 1, 1, 1, 3]
    print(move(arr))
    arr1 = [0,1,0,3,4,0,0,2,0,0,5,0]
    arr2 = [0,0,2,2,1,0,0,0,0,6,6]
    print(innerProduct(arr1, arr2))
    print(innerProduct2(arr1, arr2))
main() 