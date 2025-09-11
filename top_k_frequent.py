import unittest
from typing import List


# Top K Frequent Element

# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Input: nums = [1,1,1,2,2,3], k = 2

# Output: [1,2]

# Example 2:

# Input: nums = [1], k = 1

# Output: [1]

# Example 3:

# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

# Output: [1,2]

 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.

def topKFrequent(nums: List[int], k: int) -> List[int]:
        d = {}

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        res = []

        for i in range(k):
            res.append(max(d, key = d.get))
            d.pop(max(d, key = d.get))

        return res

class TestGroupAnagrams(unittest.TestCase):
    def test1(self):
        self.assertEqual(topKFrequent([1,1,1,2,2,3], 2), [1,2])

    def test2(self):
        self.assertEqual(topKFrequent([1], 1), [1])
    
    def test3(self):
        self.assertEqual(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2), [1,2])


if __name__ == "__main__":
    unittest.main()