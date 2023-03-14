class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        def helper(ind, nums, memo):
            for i in range(len(nums) - 1, -1, -1):
                if i == len(nums) - 1:
                    memo[i] = True
                else:
                    for j in range(nums[i]+1):
                        if i + j < len(nums):
                            if memo[i + j] == True:
                                memo[i] = True
                                break

        memo = [False for i in range(len(nums))]

        helper(0, nums, memo)
        return memo[0]