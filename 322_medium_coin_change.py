import unittest

# Coin change

# You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

# Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

# You may assume that you have an infinite number of each kind of coin.

 

# Example 1:

# Input: coins = [1,2,5], amount = 11
# Output: 3
# Explanation: 11 = 5 + 5 + 1
# Example 2:

# Input: coins = [2], amount = 3
# Output: -1
# Example 3:

# Input: coins = [1], amount = 0
# Output: 0
 

# Constraints:

# 1 <= coins.length <= 12
# 1 <= coins[i] <= 231 - 1
# 0 <= amount <= 104

def coinChange(coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        minCoins = [0 for i in range(amount+1)]

        for i in range(1, len(minCoins)):
            m = float('inf')

            for coin in coins:
                diff = i - coin
                if diff < 0:
                    break
                m = min(m, minCoins[diff]+1)
            
            minCoins[i] = m
        
        if minCoins[amount] < float('inf'):
             return minCoins[amount]
        else:
             return -1

        
       


class TestCoinChange(unittest.TestCase):
    def test1(self):
        self.assertEqual(coinChange([1, 4, 5], 12), 3)

    def test2(self):
        self.assertEqual(coinChange([1, 2, 5], 11), 3)

    def test3(self):
        self.assertEqual(coinChange([2], 3), -1)

    def test4(self):
        self.assertEqual(coinChange([1], 0), 0)


if __name__ == "__main__":
    unittest.main()