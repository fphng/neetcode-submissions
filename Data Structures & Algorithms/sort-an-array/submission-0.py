class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n <= 1:
            return nums

        def sift_down(i: int, heap_size: int) -> None:
            """Restore max-heap property starting from index i, within nums[0:heap_size]."""
            while True:
                left = 2 * i + 1
                right = left + 1
                largest = i

                if left < heap_size and nums[left] > nums[largest]:
                    largest = left
                if right < heap_size and nums[right] > nums[largest]:
                    largest = right

                if largest == i:
                    return  # heap property satisfied

                nums[i], nums[largest] = nums[largest], nums[i]
                i = largest  # continue sifting down where the element moved

        # 1) Build max heap in-place (bottom-up heapify)
        for i in range(n // 2 - 1, -1, -1):
            sift_down(i, n)

        # 2) Extract max repeatedly and place it at the end
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]  # move current max to final position
            sift_down(0, end)                        # restore heap in nums[0:end]

        return nums        