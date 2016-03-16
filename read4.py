class Solution(object):
    def __init__(self):
        self.queue = []
        
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # keep a queue, read from queue first
        ans = 0
        buf4 = ['' for _ in range(4)]
        while n:
            l = read4(buf4)
            self.queue += buf4
            left = min(len(self.queue), n - ans)
            if left == 0: return ans
            for i in range(left):
                buf[ans] = self.queue.pop(0)
                ans += 1
                n -= 1
        return ans
    
s = Solution()
