class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}  # key -> list of strings

        for s in strs:
            counts = [0] * 26
            for ch in s:
                counts[ord(ch) - ord('a')] += 1
            key = tuple(counts)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())