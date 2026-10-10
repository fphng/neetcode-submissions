class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 1) Initialize graph structures for all unique letters
        adj = defaultdict(set)   # char -> set of next chars
        indeg = {c: 0 for w in words for c in w}

        # 2) Build constraints from adjacent words
        for w1, w2 in zip(words, words[1:]):
            # Invalid if w1 starts with w2 but is longer (prefix conflict)
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""

            # Find first differing character
            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    # Add edge c1 -> c2 if it's new
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indeg[c2] += 1
                    break
            # If no break: either identical up to min length; handled by prefix rule above

        # 3) Topological sort (Kahn)
        q = deque([c for c, d in indeg.items() if d == 0])
        order = []

        while q:
            c = q.popleft()
            order.append(c)
            for nxt in adj[c]:
                indeg[nxt] -= 1
                if indeg[nxt] == 0:
                    q.append(nxt)

        # If not all letters included, there's a cycle
        return "".join(order) if len(order) == len(indeg) else ""        