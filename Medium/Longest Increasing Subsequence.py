class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #idea is that subsequence starting at index i is max (1 , 1 + subsequence at index i + 1 if index i + 1 is greater than index i)
        memo = {}
        for i in range(len(nums) - 1, -1, -1):
                memo[i] = 1
                for j in range(i+1, len(nums)):
                    if nums[i] < nums[j]:
                        memo[i] = max(memo[i], memo[j] + 1)

        print(memo)

        return max(memo.values())

