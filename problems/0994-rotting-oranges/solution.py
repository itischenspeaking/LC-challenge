class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        visited = set()
        step = 0 
        row = len(grid)
        col = len(grid[0])

        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 2:
                    q.append((i, j, step))

        while q:
            r, c, step = q.popleft()
            for dr, dc in directions:
                nr = r + dr
                nc = c + dc
                if 0 <= nr < row and 0 <= nc < col:
                    if grid[nr][nc] == 1:
                        q.append((nr, nc, step+1))
                        grid[nr][nc] = 2

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return -1

        return step
