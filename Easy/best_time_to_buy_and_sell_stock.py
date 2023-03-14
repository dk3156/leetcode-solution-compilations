class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #getting the minumum value before the current elem, and update the max profit by calculating current elem - min val, to this til end of the list, and update minimum before moving onto the next element
        max_pr = 0
        min_num = prices[0]
        for num in prices:
            max_pr = max(max_pr, num - min_num)
            min_num = min(min_num, num)
        return max_pr