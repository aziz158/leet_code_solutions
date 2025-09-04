import unittest

# Pascal's Triangle

# Given an integer numRows, return the first numRows of Pascal's triangle.

# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

# Example 1:

# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Example 2:

# Input: numRows = 1
# Output: [[1]]
 

# Constraints:

# 1 <= numRows <= 30

def generate(numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        triangle = []

        for i in range(numRows):
            if i == 0:
                  triangle.append([1])
            else:
                previous_row = triangle[i-1]
                curr_row = []
                for j in range(len(previous_row)+1):
                    if j == 0:
                        curr_row.append(1)
                    elif j == len(previous_row):
                         curr_row.append(1)
                         triangle.append(curr_row)
                    else:
                        curr_row.append(previous_row[j-1] + previous_row[j])
                
                    
        return triangle

class TestPascalTriangle(unittest.TestCase):
    def test1(self):
        self.assertEqual(generate(1), [[1]])

    def test2(self):
        self.assertEqual(generate(2), [[1], [1, 1]])

    def test3(self):
        self.assertEqual(generate(3), [[1], [1, 1], [1, 2, 1]])

    def test4(self):
        self.assertEqual(generate(4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])

    def test5(self):
        self.assertEqual(generate(5), [[1],[1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]])



if __name__ == "__main__":
    unittest.main()