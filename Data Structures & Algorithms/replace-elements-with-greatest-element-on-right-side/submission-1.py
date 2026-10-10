class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_right = -1  # last element should become -1

        for i in range(len(arr) - 1, -1, -1):
            current = arr[i]     # save original value before overwriting
            arr[i] = max_right   # replace with best seen to the right
            if current > max_right:
                max_right = current

        return arr