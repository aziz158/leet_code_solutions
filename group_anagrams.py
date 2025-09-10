import unittest
from typing import List

# Group Anagrams

# Given an array of strings strs, group the anagrams together. You can return the answer in any order.

 

# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

 

# Constraints:

# 1 <= strs.length <= 104
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.

def groupAnagrams(strs: List[str]) -> List[List[str]]:

    d = {}

    res = []

    for s in strs:

        key = ''.join(sorted(s)) 
        if key in d:
            d[key].append(s)
        else:
            d[key] = [s]
    
    
        
    for key in d:
        res.append(d[key])

    return res


class TestGroupAnagrams(unittest.TestCase):
    def test1(self):
        self.assertEqual(groupAnagrams(["eat","tea","tan","ate","nat","bat"]), [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']])

    def test2(self):
        self.assertEqual(groupAnagrams([""]), [[""]])
    
    def test3(self):
        self.assertEqual(groupAnagrams(["a"]), [["a"]])


if __name__ == "__main__":
    unittest.main()