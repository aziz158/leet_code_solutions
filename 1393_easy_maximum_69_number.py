import unittest

# # Maximum 69 number

# You are given a positive integer num consisting only of digits 6 and 9.

# Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

# Example 1:

# Input: num = 9669
# Output: 9969
# Explanation: 
# Changing the first digit results in 6669.
# Changing the second digit results in 9969.
# Changing the third digit results in 9699.
# Changing the fourth digit results in 9666.
# The maximum number is 9969.
# Example 2:

# Input: num = 9996
# Output: 9999
# Explanation: Changing the last digit 6 to 9 results in the maximum number.
# Example 3:

# Input: num = 9999
# Output: 9999
# Explanation: It is better not to apply any change.
 

# Constraints:

# 1 <= num <= 104
# num consists of only 6 and 9 digits.


def maximum69Number (num: int) -> int:

        s = str(num)
        new = ""
        pos = -1

        for i in range(len(s)):
            if s[i] == '6':
                new += '9'
                pos = i
                break
            new += s[i]
        
        if pos != -1:

            for j in range(pos+1, len(s)):
                new += s[j]
        

                
        return int(new)


class TestLPS(unittest.TestCase):
    def test1(self):
        self.assertEqual(maximum69Number(9669), 9969)

    def test2(self):
        self.assertEqual(maximum69Number(9996), 9999)

    def test3(self):
        self.assertEqual(maximum69Number(9999), 9999)


if __name__ == "__main__":
    unittest.main()