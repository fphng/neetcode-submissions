class Solution:
    def isValid(self, s: str) -> bool:
        match = {')': '(', ']': '[', '}': '{'}
        stack = []

        for ch in s:
            if ch in match:  # closing bracket
                if not stack or stack[-1] != match[ch]:
                    return False
                stack.pop()
            else:            # opening bracket
                stack.append(ch)

        return len(stack) == 0   