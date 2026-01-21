import unittest
from typing import *

# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly left rotated at an unknown index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be left rotated by 3 indices and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1
 

# Constraints:

# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -104 <= target <= 104

def search(nums: List[int], target: int) -> int:

    for i in range(len(nums)):
        if target == nums[i]:
            return i
        
    
    return -1




class TestSearch(unittest.TestCase):
    def test1(self):
        self.assertEqual(search([4,5,6,7,0,1,2], 0), 4)

    def test2(self):
        self.assertEqual(search([4,5,6,7,0,1,2], 3), -1)

    def test3(self):
        self.assertEqual(search([1], 0), -1)


if __name__ == "__main__":
    unittest.main()