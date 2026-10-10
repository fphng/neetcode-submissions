class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_l = min(len(s) for s in strs)

        for i in range(min_l):
            k = strs[0][i]
            for s in strs[1:]:
                if s[i] != k:
                    return strs[0][:i]
        return strs[0][:min_l]
