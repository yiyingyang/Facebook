def flattenArray(arr):
    
    # edge cases
    if len(arr) == 0: return []
    
    # regular case
    ans = []
    for i in arr:
        if isinstance(i, int):
            ans.append(i)
        else:
            for j in flattenArray(i):
                ans.append(j)
    return ans

def main():
    print(flattenArray([1,2,[3,[4,[5,6,[7]]]]]))
    
main()