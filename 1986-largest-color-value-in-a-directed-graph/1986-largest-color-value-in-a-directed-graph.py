from collections import deque, defaultdict
from typing import List

class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        graph = defaultdict(list)
        indegree = [0] * n

        # Build the graph
        for u, v in edges:
            graph[u].append(v)
            indegree[v] += 1

        # Initialize DP array: count[i][c] = max count of color 'a'+c at node i
        count = [[0] * 26 for _ in range(n)]

        # Queue for topological sort (nodes with indegree 0)
        queue = deque()
        for i in range(n):
            if indegree[i] == 0:
                queue.append(i)
                count[i][ord(colors[i]) - ord('a')] = 1

        visited = 0
        max_color_val = 0

        # BFS traversal
        while queue:
            node = queue.popleft()
            visited += 1
            for neighbor in graph[node]:
                for c in range(26):
                    # Update color count for neighbor
                    count[neighbor][c] = max(count[neighbor][c],
                                             count[node][c] + (1 if c == ord(colors[neighbor]) - ord('a') else 0))
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

            # Track global max
            max_color_val = max(max_color_val, max(count[node]))

        # If not all nodes were visited, a cycle exists
        return max_color_val if visited == n else -1
