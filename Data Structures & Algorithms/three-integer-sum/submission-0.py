class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:  # skip duplicate anchors
                continue

            seen = set()
            for j in range(i + 1, n):
                need = -nums[i] - nums[j]
                if need in seen:
                    # nums is sorted and j increases, so (nums[i], need, nums[j]) is nondecreasing
                    res.add((nums[i], need, nums[j]))
                seen.add(nums[j])

        return [list(t) for t in res]       