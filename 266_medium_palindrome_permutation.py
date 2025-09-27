import unittest

# Palindrom permutation

# Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

 

# Example 1:

# Input: s = "code"
# Output: false
# Example 2:

# Input: s = "aab"
# Output: true
# Example 3:

# Input: s = "carerac"
# Output: true
 

# Constraints:

# 1 <= s.length <= 5000
# s consists of only lowercase English letters.

def canPermutePalindrome(s: str) -> bool:

    d = {}

    for ch in s:

        if ch in d:
            d[ch] += 1
        else:
            d[ch] = 1


    count = 0

    for key in d:

        if d[key] % 2 != 0:
            count += 1
            if count > 1:
                return False
    
    return True





print(canPermutePalindrome("carerac"))