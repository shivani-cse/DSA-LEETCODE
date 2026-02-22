class Solution:
    def binaryGap(self, n: int) -> int:
        ans = 0
        prev = -1  # position of last '1'
        pos = 0    # current bit index

        while n > 0:
            if n & 1 == 1:    # check current bit
                if prev >= 0:
                    ans = max(ans, pos - prev)
                prev = pos
            n >>= 1
            pos += 1

        return ans
        