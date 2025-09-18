import unittest

# Majority element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
 

# Constraints:

# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

def majorityElement(nums):
    
    d = {}

    for i in nums:
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    
    return max(d, key = d.get)
    

class TestMajorityElement(unittest.TestCase):
    def test1(self):
        self.assertEqual(majorityElement([3,2,3]), 3)

    def test2(self):
        self.assertEqual(majorityElement([2,2,1,1,1,2,2]), 2)



if __name__ == "__main__":
    unittest.main()