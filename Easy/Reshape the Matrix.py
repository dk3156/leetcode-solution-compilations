class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        #so r is the number of elem in the list, and and c is the number of elem in element list. we should be able to expand or shrink the element list to the number c, and the whole list to the number r, by combining or divisinf the elem list. count the number of elems in the entire list and calculate. we know we have four numbers in the example. r = 1 and c = 4 can make four element. 1 * 4 = 4. 
        # This means that r * c should be equal to rows and cols in the original list. if not, cannot make it.
        # if you have 2 elems in the column, and you need to expand it to 4, you need to bring the elem in the other list to the original list. Or, you need to create another list that contains the list that satisfies the condition. ==> if you have 1 and 4 as requirement, you need to have one list with four elem. 
        # So create a list and populate them. 
        # if you have c = n, but cols = k, iterate through cols n / k times. it will give you n items at the end.
        # in the same sense, if you have r = n and rows = k, n / k will give you how many list you need.
        # when n is   
        rows = len(mat)
        cols = len(mat[0])
        result = []
        arr = []
        i = 0
        if rows * cols == r * c:
            for row in mat:
                for elem in row:
                    arr.append(elem)
                    i += 1
                    if (i == c):
                        result.append(arr)
                        arr = []
                        i = 0
            return result
        else:
            return mat
