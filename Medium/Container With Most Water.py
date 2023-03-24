class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #volume for max distance VS O(1)
        #find max volume for a tallest element O(n) for finding tallest
        # + O(n) for comparing volume
        i = 0
        j = len(height) - 1
        max_vol = 0
        while i != j:
            if height[i] < height[j]:
                shorter = i
                i += 1
            else:
                shorter = j
                j -= 1
            max_vol = max((j - i + 1) * height[shorter], max_vol)
        
        return max_vol