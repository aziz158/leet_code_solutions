import unittest

# Longest Palindromic Substring

# Medium
# Topics
# conpanies icon
# Companies
# Hint
# Given a string s, return the longest palindromic substring in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"
 

# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

def longestPalindrome(s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 1:
            return s


        o = odd(s)
        e = even(s)
        return o if len(o) >= len(e) else e


def odd(s):
    d = {}

    for i in range(len(s) - 1):
        
        if i + 1 < len(s) and s[i] == s[i+1]:  
            m1 = i
            m2 = i+1
            
            sub = s[m1:m2+1]                 
            d[len(sub)] = sub
            l = m1-1
            r = m2+1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                sub = s[l:r+1]                
                l -= 1
                r += 1
                d[len(sub)] = sub

        sub = s[i]
        d[len(sub)] = sub
        l = i-1
        r = i+1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            sub = s[l:r+1]                    
            l -= 1
            r += 1
            d[len(sub)] = sub
        
    # print(d)
    return d[max(d)]

def even(s):
    d = {}

    if len(s) == 2:
        if s[0] == s[1]:
            return s
        else:
            return s[0]

    for i in range(1, len(s)):                 
        m1 = i-1
        m2 = i

        if s[m1] != s[m2]:
            sub = s[i]
            d[len(sub)] = sub
            l = i-1
            r = i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                sub = s[l:r+1]               
                l -= 1
                r += 1
                d[len(sub)] = sub
            continue
        
        sub = s[m1:m2+1]                      
        d[len(sub)] = sub
        l = m1-1
        r = m2+1

        while l >= 0 and r < len(s) and s[l] == s[r]:
            sub = s[l:r+1]                   
            l -= 1
            r += 1
            d[len(sub)] = sub

    return d[max(d)]
        
        
             
            

class TestLPS(unittest.TestCase):
    def test1(self):
        self.assertEqual(longestPalindrome("babad"), "aba")

    def test2(self):
        self.assertEqual(longestPalindrome("cbbd"), "bb")

    def test3(self):
        self.assertEqual(longestPalindrome("aaaaa"), "aaaaa")

    def test4(self):
        self.assertEqual(longestPalindrome("caaaaa"), "aaaaa")
    
    def test5(self):
        self.assertEqual(longestPalindrome("ac"), "a")

if __name__ == "__main__":
    unittest.main()