
import unittest

# Find the index of the first occurence of the string

# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

def strStr(haystack: str, needle: str) -> int:

    res = -1

    if len(haystack) < len(needle):
        return res

    for ch in range(len(haystack)):

        if haystack[ch] == needle[0]:

            l = len(needle)
            buffer = needle

            i = 0

            while i < l:

                if ch + i >= len(haystack):
                    break
                elif haystack[ch + i] != needle[i]:
                    break
                
                buffer = buffer[1:]
                i += 1
            
            if buffer == "":
                return ch

    return res


print(strStr("mississippi", "issipi"))

class TestStr(unittest.TestCase):
    def test1(self):
        self.assertEqual(strStr("sadbutsad", "sad"), 0)

    def test2(self):
        self.assertEqual(strStr("leetcode", "leeto"), -1)

    def test3(self):
        self.assertEqual(strStr("mississippi", "issipi"), -1)

    def test4(self):
        self.assertEqual(strStr("sadbutsad", "but"), 3)


if __name__ == "__main__":
    unittest.main()