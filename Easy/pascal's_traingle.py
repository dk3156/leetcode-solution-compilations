class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        #[1] [1,1] [1,2,1] [1,3,3,1] [1,4,6,4,1]
        #first elem and lst elem always 1
        #second and second to last is 1 + the elem right after that
        #third and third to the lst is second + third, second + third to last
        # repeat
        result = []
        temp = []
        for i in range(1, numRows + 1):
            j = 0
            arr = []
            while j < i:
                if j == 0:
                    arr.append(1)
                elif j == i - 1:
                    arr.append(1)
                else:
                    k = temp[j - 1] + temp [j]
                    arr.append(k)
                j += 1
            result.append(arr)
            temp = arr

        return result

    