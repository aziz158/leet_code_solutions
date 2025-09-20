import unittest

# Search 2D Matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

 

# Example 1:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true


# Example 2:

# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
 

# Constraints:

# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -104 <= matrix[i][j], target <= 104

def searchMatrix(matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        for row in matrix:

            l = 0
            r = len(row)

            while l < r:

                m = (l + r)//2

                if row[m] > target:
                    r = m
                elif row[m] < target:
                    l = m + 1
                elif row[m] == target:
                    return True
        
        return False

class TestSearchMatrix(unittest.TestCase):
    def test1(self):
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True)

    def test2(self):
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 2), False)

    def test3(self):
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False)


if __name__ == "__main__":
    unittest.main()