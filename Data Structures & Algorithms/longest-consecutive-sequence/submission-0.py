class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        best = 0
        for i in s:
            if i - 1 not in s:
                j = i
                while j in s:
                    j += 1
                best = max(best, j - i)
        return best