import unittest

# Longest Common Prefix

# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
 

# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters if it is non-empty.

strs = ["flower","flow","flight"]

def longestCommonPrefix(strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
                return ""
        if len(strs) == 1:
                return strs[0]

        prefix = strs[0]

        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[0:len(prefix)-1]
                if prefix == "":
                      return ""
                
        return prefix

class TestLCP(unittest.TestCase):
    def test1(self):
        self.assertEqual(longestCommonPrefix(["flower","flow","flight"]), "fl")

    def test2(self):
        self.assertEqual(longestCommonPrefix(["dog","racecar","car"]), "")





if __name__ == "__main__":
    unittest.main()
            
                

