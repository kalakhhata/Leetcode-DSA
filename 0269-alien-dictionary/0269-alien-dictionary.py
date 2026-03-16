from collections import defaultdict, deque

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        adj = defaultdict(set)
        indeg = {c:0 for word in words for c in word}

        # build graph
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]

            if len(w1) > len(w2) and w1.startswith(w2):
                return ''

            for c1, c2 in zip(w1, w2):
                if c1 != c2:
                    if c2 not in adj[c1]:
                        adj[c1].add(c2)
                        indeg[c2] += 1
                    break

        # topological sort
        q = deque()
        for c in indeg:
            if indeg[c] == 0:
                q.append(c)

        res = ""

        while q:
            c = q.popleft()
            res += c

            for ne in adj[c]:
                indeg[ne] -= 1
                if indeg[ne] == 0:
                    q.append(ne)

        if len(res) != len(indeg):
            return ''

        return res