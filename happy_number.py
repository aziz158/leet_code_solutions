import unittest

# Happy Number

# Write an algorithm to determine if a number n is happy.

# A happy number is a number defined by the following process:

# Starting with any positive integer, replace the number by the sum of the squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# Return true if n is a happy number, and false if not.

 

# Example 1:

# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# Example 2:

# Input: n = 2
# Output: false
 

# Constraints:

# 1 <= n <= 231 - 1

def isHappy(n):
    seen=set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(digits)**2 for digits in str(n))
    return n == 1

class TestRomanToInt(unittest.TestCase):
    def test1(self):
        self.assertEqual(isHappy(19), True)

    def test2(self):
        self.assertEqual(isHappy(2), False)



if __name__ == "__main__":
    unittest.main()