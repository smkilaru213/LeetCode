
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        ret = 0

        def dfs(row, col):
            # Stop if outside the grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Stop if water or already visited
            if grid[row][col] == "0":
                return

            # Mark this land as visited
            grid[row][col] = "0"

            # Explore all four directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Check every cell in the grid
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    ret += 1
                    dfs(row, col)

        return ret