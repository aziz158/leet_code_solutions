import unittest
from typing import List

# Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

 

# Example 1:

# Input: nums = [1,2,3]
# Output: 6
# Example 2:

# Input: nums = [1,2,3,4]
# Output: 24
# Example 3:

# Input: nums = [-1,-2,-3]
# Output: -6
 

# Constraints:

# 3 <= nums.length <= 104
# -1000 <= nums[i] <= 1000


def maximumProduct(nums: List[int]) -> int:

    nums.sort()
        
    option1 = nums[-1] * nums[-2] * nums[-3]
        
    option2 = nums[0] * nums[1] * nums[-1]
        
    return max(option1, option2)



class TestMaxProd(unittest.TestCase):
    def test1(self):
        self.assertEqual(maximumProduct([2,1,4,7,3,2,5]), 140)

    def test2(self):
        self.assertEqual(maximumProduct([2,2,2]), 8)

    def test3(self):
        self.assertEqual(maximumProduct([2,3,1,2,3,4,5,6]), 120)
    



if __name__ == "__main__":
    unittest.main()
