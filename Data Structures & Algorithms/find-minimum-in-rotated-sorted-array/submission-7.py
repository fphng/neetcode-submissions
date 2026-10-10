class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        
        # Great initial check! If it's already sorted, the first element is the min.
        if nums[r] >= nums[l]:
            return nums[l]
            
        while l <= r:
            m = l + ((r - l) // 2)
            
            # Check if the drop is right after m
            if m < len(nums) - 1 and nums[m] > nums[m + 1]:
                return nums[m + 1]
                
            # Check if the drop is exactly at m
            if m > 0 and nums[m - 1] > nums[m]:
                return nums[m]
                
            # If we haven't found the drop, decide which half to discard
            if nums[m] >= nums[l]:
                # Left half is sorted, inflection point is to the right
                l = m + 1
            else:
                # Right half is sorted, inflection point is to the left
                r = m - 1