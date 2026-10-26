class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0:
                    continue

                total = grid[r][c]
                stack = [(r, c)]
                grid[r][c] = 0

                while stack:
                    row, col = stack.pop()

                    for dr, dc in directions:
                        nr, nc = row + dr, col + dc

                        if (0 <= nr < m and 0 <= nc < n
                                and grid[nr][nc] > 0):
                            total += grid[nr][nc]
                            grid[nr][nc] = 0
                            stack.append((nr, nc))

                if total % k == 0:
                    count += 1

        return count