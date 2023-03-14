
INF = 2**31 - 1

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = [INF for i in range(amount + 1)]
        memo[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    memo[a] = min(memo[a], 1 + memo[a - c])

        return memo[amount] if memo[amount] != INF else -1

