import unittest

# Valid Parenthesis

# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

def isValid(s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
    
        d = {'}':'{', ']':'[', ')':'(' }

        
        for i in s:
            if i in d.values():
                stack.append(i)
            elif i in d.keys():
                if not stack or stack.pop() != d[i]:
                    return False

        return len(stack) == 0

class TestTwoSum(unittest.TestCase):
    def test1(self):
        self.assertEqual(isValid("()"), True)

    def test2(self):
        self.assertEqual(isValid("()[]{}"), True)

    def test3(self):
        self.assertEqual(isValid("(]"), False)

    def test4(self):
        self.assertEqual(isValid("([])"), True)

    def test5(self):
        self.assertEqual(isValid("([)]"), False)


if __name__ == "__main__":
    unittest.main()