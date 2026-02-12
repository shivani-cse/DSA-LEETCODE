class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        ans = 1
        
        for i in range(n):
            freq = [0]*26
            for j in range(i, n):
                freq[ord(s[j]) - 97] += 1
                
                # collect non-zero frequencies
                counts = [c for c in freq if c > 0]
                
                # check if all frequencies are equal
                if len(set(counts)) == 1:
                    ans = max(ans, j - i + 1)
        
        return ans


