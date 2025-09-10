import unittest

# Find the Duplicate number

# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and using only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3
# Example 3:

# Input: nums = [3,3,3,3,3]
# Output: 3
 

# Constraints:

# 1 <= n <= 105
# nums.length == n + 1
# 1 <= nums[i] <= n
# All the integers in nums appear only once except for precisely one integer which appears two or more times.
 

def findDuplicate(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = {}

        for i in nums:
            if i in h:
                return i
            h[i] = i

class TestFindDuplicate(unittest.TestCase):
    def test1(self):
        self.assertEqual(findDuplicate([1,3,4,2,2]), 2)

    def test2(self):
        self.assertEqual(findDuplicate([3,1,3,4,2]), 3)

    def test3(self):
        self.assertEqual(findDuplicate([3,3,3,3,3]), 3)


if __name__ == "__main__":
    unittest.main()