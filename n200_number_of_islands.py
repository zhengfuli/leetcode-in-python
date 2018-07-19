class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        check = [[not bool(int(i)) for i in grid[j]] for j in range(len(grid))]

        def checkIsland(x, y):
            queue = [(x, y)]
            while queue:
                i, j = queue.pop()
                for (row, col) in [(i-1, j), (i, j-1), (i, j+1), (i+1, j)]:
                    if 0 <= row < len(check) and 0 <= col < len(check[0]):
                        if not check[row][col]:
                            check[row][col] = not check[row][col]
                            queue.append((row, col))
            return

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1" and not check[i][j]:
                    check[i][j] = not check[i][j]
                    count += 1
                    checkIsland(i, j)

        return count

if __name__ == '__main__':
    tb = Solution()
    print(tb.numIslands([["0", "0", "1", "1", "1", "0", "0"],
                         ["0", "0", "1", "0", "1", "0", "0"],
                         ["1", "0", "0", "0", "0", "0", "1"],
                         ["1", "0", "1", "1", "1", "0", "0"],
                         ["0", "0", "1", "1", "1", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "1", "0", "0"]]))