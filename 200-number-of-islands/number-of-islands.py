class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        ret = 0

        def dfs(row, col):
            # Check if we're outside the grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Stop if water or already visited
            if grid[row][col] == "0" or (row, col) in visited:
                return

            # Mark current cell as visited
            visited.add((row, col))

            # Explore all four directions
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        # Go through every cell
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    ret += 1
                    dfs(row, col)

        return ret