import unittest

# Merge Sorted array:

# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

# Merge nums1 and nums2 into a single array sorted in non-decreasing order.

# The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

# Example 1:

# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
# Example 2:

# Input: nums1 = [1], m = 1, nums2 = [], n = 0
# Output: [1]
# Explanation: The arrays we are merging are [1] and [].
# The result of the merge is [1].
# Example 3:

# Input: nums1 = [0], m = 0, nums2 = [1], n = 1
# Output: [1]
# Explanation: The arrays we are merging are [] and [1].
# The result of the merge is [1].
# Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

# Constraints:

# nums1.length == m + n
# nums2.length == n
# 0 <= m, n <= 200
# 1 <= m + n <= 200
# -109 <= nums1[i], nums2[j] <= 109

def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if m == 0:
        nums1[:] = nums2
        return nums1
    elif n == 0:
        return nums1
    else:
        
        if len([0 for i in range(m + nums1.count(0) - len(nums1))]) != 0:
            nums1[:] = [i for i in nums1 if i != 0] + [0 for i in range(m + nums1.count(0) - len(nums1))]
        else:
            nums1[:] = [i for i in nums1 if i != 0]
        nums1[:] = sorted(nums1 + nums2)
        return nums1
    
print(merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3))

class TestMergeSortArray(unittest.TestCase):
    def test1(self):
        self.assertEqual(merge([-1,0,0,3,3,3,0,0,0], 6, [1,2,2], 3), [-1, 0, 0, 1, 2, 2, 3, 3, 3])

    def test2(self):
        self.assertEqual(merge([1,2,3,0,0,0], 3, [2,5,6], 3), [1,2,2,3,5,6])

    def test3(self):
        self.assertEqual(merge([1], 1, [], 0), [1])

    def test4(self):
        self.assertEqual(merge([0], 0, [1], 1), [1])



if __name__ == "__main__":
    unittest.main()