class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # XOR all indices 0..n and all nums
        for i, x in enumerate(nums):
            ans ^= i
            ans ^= x

        ans ^= n  # include n (since enumerate only gives 0..n-1)
        return ans