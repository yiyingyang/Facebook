import random
import unittest

def shuffle(arr):   
    if not arr or len(arr) == 1:
        return arr
    
    for i in reversed(range(len(arr))):
        x = random.randint(0, i)
        if x != i:
            arr[x], arr[i] = arr[i], arr[x]
    
    return arr

class MyTest(unittest.TestCase):
    def test(self):
        assert 1+1 == 2
    
if __name__ == '__main__':
    unittest.main()