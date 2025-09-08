import unittest

# Climbing Stairs

# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:

# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
 

# def climbStairs(n):
#         """
#         :type n: int
#         :rtype: int
#         """

#         return climb_Stairs(0, n)

# def climb_Stairs(i, n):
#     if i > n:
#         return 0
#     if i == n:
#         return 1
#     return climb_Stairs(i + 1, n) + climb_Stairs(i + 2, n)


def climbStairs(n):
        """
        :type n: int
        :rtype: int
        """


        if n == 1:
            return 1
        


        dp = [None for _ in range(n+1)]

      
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
 
            
            dp[i] = dp[i-1] + dp[i-2]
            
        return dp[n]




class TestClimbStairs(unittest.TestCase):
    def test1(self):
        self.assertEqual(climbStairs(2), 2)

    def test2(self):
        self.assertEqual(climbStairs(3), 3)

    def test3(self):
        self.assertEqual(climbStairs(4), 5)


if __name__ == "__main__":
    unittest.main()