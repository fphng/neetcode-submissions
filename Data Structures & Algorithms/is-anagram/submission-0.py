class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        counts = [0] * 26
        base = ord('a')

        for ch in s:
            counts[ord(ch) - base] += 1
        for ch in t:
            idx = ord(ch) - base
            counts[idx] -= 1
            if counts[idx] < 0:   # t has this char too many times
                return False

        return True