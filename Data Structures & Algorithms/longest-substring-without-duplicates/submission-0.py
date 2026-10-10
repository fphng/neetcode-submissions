class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}   # char -> last index seen
        l = 0
        best = 0

        for r, ch in enumerate(s):
            if ch in last and last[ch] >= l:
                l = last[ch] + 1  # jump left boundary past duplicate

            last[ch] = r
            best = max(best, r - l + 1)

        return best
        