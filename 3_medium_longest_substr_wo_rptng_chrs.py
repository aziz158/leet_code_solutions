import unittest

# Longest substring without repeating characters

# Given a string s, find the length of the longest substring without duplicate characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

def lengthOfLongestSubstring(s):
        """
        :type s: str
        :rtype: int
        """
        d = {}          # char -> last index seen
        left = 0        # start of the current window (inclusive)
        best = 0        # length of the longest window seen so far

        for right, ch in enumerate(s):           # scan s from left to right
            if ch in d and d[ch] >= left:        # duplicate inside the window?
                left = d[ch] + 1                 # move window start past prior ch
            d[ch] = right                        # update ch's most recent index
            best = max(best, right - left + 1)   # window length -> update best
        return best


class TestLengthOfLongestSubstring(unittest.TestCase):
     
    def test1(self):
        self.assertEqual(lengthOfLongestSubstring("abcabcbb"), 3)
     
    def test2(self):
        self.assertEqual(lengthOfLongestSubstring("bbbbb"), 1)
    
    def test3(self):
        self.assertEqual(lengthOfLongestSubstring("pwwkew"), 3)

    def test4(self):
        self.assertEqual(lengthOfLongestSubstring("aab"), 2)
    
    def test5(self):
        self.assertEqual(lengthOfLongestSubstring("bvbf"), 3)


if __name__ == "__main__":
    unittest.main()