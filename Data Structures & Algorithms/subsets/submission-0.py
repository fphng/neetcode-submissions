class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []

        def dfs(start: int) -> None:
            # Every state of `subset` is a valid subset
            res.append(subset.copy())

            for i in range(start, len(nums)):
                subset.append(nums[i])     # choose nums[i]
                dfs(i + 1)                 # explore further choices
                subset.pop()               # undo choice (backtrack)

        dfs(0)
        return res