import unittest
from typing import *

# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

def exist(board: List[List[str]], word: str) -> bool:

    m = len(board)
    n = len(board[0])
    W = len(word)

    if m == 1 and n == 1:
        return board[0][0] == word
    
    def backtrack(pos, index):
        i, j = pos

        if index == W:
            return True
        
        if board[i][j] != word[index]:
            return False
        
        char = board[i][j]
        board[i][j] = "#"

        for i_off, j_off in [(0,1), (1,0), (0,-1), (-1, 0)]:
            r, c = i + i_off, j + j_off
            if 0 <= r < m and 0 <= c < n:
                if backtrack((r, c), index+1):
                    return True
                
        board[i][j] = char
        return False


    for i in range(m):
        for j in range(n):
            if backtrack((i, j), 0):
                return True

    return False


class TestWS(unittest.TestCase):
    def test1(self):
        self.assertEqual(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True)

    def test2(self):
        self.assertEqual(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True)

    def test3(self):
        self.assertEqual(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), False)


if __name__ == "__main__":
    unittest.main()