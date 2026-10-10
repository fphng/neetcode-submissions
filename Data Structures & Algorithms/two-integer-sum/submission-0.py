class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, x in enumerate(nums):
            remain = target - x
            if remain in checked:
                return [checked[remain],i]
            
            if x not in checked:
                checked[x] = i
        return []