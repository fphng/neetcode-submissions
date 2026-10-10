class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        n = len(s)

        while i < n:
            # 1) read length up to '#'
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])

            # 2) read the next `length` characters as the string
            start = j + 1
            end = start + length
            res.append(s[start:end])

            # 3) move i to the start of the next encoded chunk
            i = end

        return res