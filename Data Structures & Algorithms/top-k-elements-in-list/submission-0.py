class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) frequency map
        freq = {}
        for x in nums:
            freq[x] = freq.get(x, 0) + 1

        # 2) buckets: index = frequency, value = list of numbers with that frequency
        buckets = [[] for _ in range(len(nums) + 1)]
        for val, count in freq.items():
            buckets[count].append(val)

        # 3) collect from highest frequency down
        res = []
        for count in range(len(nums), 0, -1):
            for val in buckets[count]:
                res.append(val)
                if len(res) == k:
                    return res