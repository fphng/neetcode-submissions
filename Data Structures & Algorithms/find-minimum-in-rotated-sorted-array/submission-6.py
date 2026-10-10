class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
# If the array is not rotated (or has only 1 element)
        if nums[r] >= nums[l]:
            return nums[l]
            
        while l < r:
            m = l + ((r - l) // 2)
            
            # If the mid element is strictly greater than the rightmost element,
            # the pivot (minimum) must be in the right half.
            if nums[m] > nums[r]:
                l = m + 1
            # Otherwise, the minimum is at 'm' or in the left half.
            else:
                r = m
                
        # When l == r, we have narrowed our search down to the minimum element
        return nums[l]
        