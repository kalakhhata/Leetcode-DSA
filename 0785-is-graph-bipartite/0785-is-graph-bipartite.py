from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means uncolored

        for node in range(n):
            if color[node] == -1:
                if not self.check(node, color, graph):
                    return False
        
        return True

    def check(self, start, color, graph):
        q = deque([start])
        color[start] = 0

        while q:
            node = q.popleft()

            for ne in graph[node]:
                if color[ne] == -1:
                    color[ne] = 1 - color[node]
                    q.append(ne)
                elif color[ne] == color[node]:
                    return False

        return True