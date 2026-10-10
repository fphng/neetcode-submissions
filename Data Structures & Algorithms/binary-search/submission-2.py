class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        if nums[l] == target:
            return l
        if nums[r] == target:
            return r
        while l < r - 1:
            mid = l + ((r - l)//2)
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid
            else:
                return mid
        return -1     
        