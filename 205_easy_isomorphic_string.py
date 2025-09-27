import unittest

# Isomorphic string

# Given two strings s and t, determine if they are isomorphic.

# Two strings s and t are isomorphic if the characters in s can be replaced to get t.

# All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

# Example 1:

# Input: s = "egg", t = "add"

# Output: true

# Explanation:

# The strings s and t can be made identical by:

# Mapping 'e' to 'a'.
# Mapping 'g' to 'd'.
# Example 2:

# Input: s = "foo", t = "bar"

# Output: false

# Explanation:

# The strings s and t can not be made identical as 'o' needs to be mapped to both 'a' and 'r'.

# Example 3:

# Input: s = "paper", t = "title"

# Output: true

 

# Constraints:

# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.

def isIsomorphic(s: str, t: str) -> bool:

    d = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        a, b = s[i], t[i]

        if ('s', a) in d and d[('s', a)] != b:
            return False

        if ('t', b) in d and d[('t', b)] != a:
            return False

        d[('s', a)] = b
        d[('t', b)] = a
    
   
    word = ""
    for ch in s:
        word += d[('s', ch)]
    return word == t


print(isIsomorphic('paper', 'title'))

