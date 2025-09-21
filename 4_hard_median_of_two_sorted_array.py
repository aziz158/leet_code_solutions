import unittest
from typing import List

# Median of two sorted array

# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

# The overall run time complexity should be O(log (m+n)).

 

# Example 1:

# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:

# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

# Constraints:

# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:

    nums3 = nums1 + nums2
    nums3.sort()

    if len(nums3) % 2 != 0:
        return float(nums3[len(nums3)//2])
    else:
        return float((nums3[len(nums3)//2] + nums3[(len(nums3)//2)-1])/2)

    



print(findMedianSortedArrays([1,2], [3,4]))

class TestFindMedian(unittest.TestCase):
    def test1(self):
        self.assertEqual(findMedianSortedArrays([1,3], [2]), 2.0)

    def test2(self):
        self.assertEqual(findMedianSortedArrays([1,2], [3,4]), 2.5)

if __name__ == "__main__":
    unittest.main()