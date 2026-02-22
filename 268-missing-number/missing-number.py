class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        v=n*(n+1)//2
        actual_sum=sum(nums)
        return v-actual_sum