class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        codes=set()
        for i in range(len(s)-k+1):
            codes.add(s[i:i+k])
        total=2**k

        if len(codes)==total:
            return True
        else:
            return False

        