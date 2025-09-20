import unittest
from typing import List

# Rotting oranges

# You are given an m x n grid where each cell can have one of three values:

# 0 representing an empty cell,
# 1 representing a fresh orange, or
# 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

 

# Example 1:


# Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: grid = [[0,2]]
# Output: 0
# Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Constraints:

# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 10
# grid[i][j] is 0, 1, or 2.

def orangesRotting(grid: List[List[int]]) -> int:
        
        if not grid:
            return None

        
        
        m = len(grid)
        n = len(grid[0])
        q = []
        visited = set()
        fresh = 0


        def extendRot(i,j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1 or (i,j) in visited:
                return
            
            visited.add((i,j))
            q.append([i,j])

        for i in range(m):
            for j in range (n):
                if grid[i][j] == 2:
                    q.append([i,j])
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    fresh += 1


        if fresh == 0:
            return 0                       # e.g., [[0,0,0,0]] or no fresh anywhere
        if not q:                          # fresh exists but no source to rot
            return -1


        minute = 0

        while q:
            for x in range(len(q)):
                i, j = q.pop(0)
                grid[i][j] = 2
                extendRot(i, j+1)
                extendRot(i, j-1)
                extendRot(i-1, j)
                extendRot(i+1, j)

            minute += 1
        

        for i in range(m):
            for j in range (n):
                if grid[i][j] == 1:
                    return -1

        return minute-1

class TestRottingOranges(unittest.TestCase):
    def test1(self):
        self.assertEqual(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]), 4)

    def test2(self):
        self.assertEqual(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]), -1)

    def test3(self):
        self.assertEqual(orangesRotting([[0,2]]), 0)


if __name__ == "__main__":
    unittest.main()