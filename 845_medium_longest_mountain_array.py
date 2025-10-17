import unittest
from typing import List

# Longest Mountain Array

# You may recall that an array arr is a mountain array if and only if:

# arr.length >= 3
# There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
# Given an integer array arr, return the length of the longest subarray, which is a mountain. Return 0 if there is no mountain subarray.

 

# Example 1:

# Input: arr = [2,1,4,7,3,2,5]
# Output: 5
# Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
# Example 2:

# Input: arr = [2,2,2]
# Output: 0
# Explanation: There is no mountain.
 

# Constraints:

# 1 <= arr.length <= 104
# 0 <= arr[i] <= 104

def longestMountain(arr: List[int]) -> int:

    n = len(arr)
    ans = 0
    i = 1
    while i < n-1:
        if arr[i-1] < arr[i] > arr[i+1]:       
            l = i-1
            r = i+1
            while l > 0 and arr[l-1] < arr[l]: l -= 1
            while r < n-1 and arr[r] > arr[r+1]: r += 1
            ans = max(ans, r - l + 1)
            i = r                                
        else:
            i += 1
    return ans


class TestFindDuplicate(unittest.TestCase):
    def test1(self):
        self.assertEqual(longestMountain([2,1,4,7,3,2,5]), 5)

    def test2(self):
        self.assertEqual(longestMountain([2,2,2]), 0)

    def test3(self):
        self.assertEqual(longestMountain([2,3,1,2,3,4,5,6]), 3)
    
    def test4(self):
        self.assertEqual(longestMountain([0]), 0)


if __name__ == "__main__":
    unittest.main()


