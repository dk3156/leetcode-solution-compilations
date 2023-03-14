class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        prev = 0
        for num in nums:
            prev = max(prev + num, num)
            max_sum = max(prev, max_sum) 
            print(prev)

        return max_sum

            
        
                
            
            