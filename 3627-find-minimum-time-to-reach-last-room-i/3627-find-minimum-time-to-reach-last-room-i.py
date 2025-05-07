class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n, m = len(moveTime), len(moveTime[0])
        heap = [(0, 0, 0)]  # (time, row, col)
        visited = [[float('inf')] * m for _ in range(n)]
        visited[0][0] = 0

        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            time, x, y = heapq.heappop(heap)
            if (x, y) == (n - 1, m - 1):
                return time

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    new_time = max(time + 1, moveTime[nx][ny])
                    if new_time == moveTime[nx][ny]:
                        new_time += 1
                    if visited[nx][ny] > new_time:
                        visited[nx][ny] = new_time
                        heapq.heappush(heap, (new_time, nx, ny))

        return -1