class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # take 1 step -> climbStairs(n-1), climbStairs(n-2)
        # if n == 1 or 2 
        # n - 1 
        # n - 2
        # (3) -> (1) -> 1
        # (3) -> (2) -> 1
        # (3) -> (
        def helper(n, memo):
            if n == 1 or n == 2:
                return n
            if n in memo:
                return memo[n]
            else:
                ans = helper(n - 1, memo) + helper(n - 2, memo)
                memo[n] = ans
                return ans

        return helper(n, {})
        