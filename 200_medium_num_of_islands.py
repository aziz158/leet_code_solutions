import unittest
from typing import List

# Number of Islands

# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

# Example 1:

# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
# Example 2:

# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

def numIslands(grid: List[List[str]]) -> int:

    m = len(grid)
    n = len(grid[0])

    def dfs(i, j):

        if i < 0 or i >=m or j < 0 or j >= n or grid[i][j] == '0':
            return
        else:
            grid[i][j] = '0'
            dfs(i, j+1)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i-1, j)

    
    islands = 0

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '1':
                islands += 1
                dfs(i, j)
    
    return islands


class TestNumIslands(unittest.TestCase):
    def test1(self):
        self.assertEqual(numIslands([
   ["1","1","0","0","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]
 ]), 3)

    def test2(self):
        self.assertEqual(numIslands([
   ["1","1","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","0","0","0"]
 ]), 1)
        
    def test3(self):
        self.assertEqual(numIslands([
   ["1","0","1","1","0"],
   ["1","1","0","1","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","1"]
 ]), 4)

    def test4(self):
        self.assertEqual(numIslands([
    ["1","0","1","0","1"],
    ["0","1","0","1","0"],
    ["1","0","1","0","1"],
    ["0","1","0","1","0"]
 ]), 10)

if __name__ == "__main__":
    unittest.main()
