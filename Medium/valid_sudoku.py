class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # board[0][j] ->checking each row <- j in range(9)
        # board[i][0] -> checking each column <- i in range(9)

        # board[i][j] -> i in range 3, j in range 3 <- checking 3 by 3
        # -> i in range 3 - 6, j in range 3
        # combination: (0 - 3, 0 - 3) (3 - 6, 0 - 3) (6 - 9, 0 - 3)
        # ( 0 - 3, 3 - 6) (3 - 6, 3 - 6) (6 - 9, 3 - 6)

        dic = set()

        for i in range(9):
            for j in range(9):
                k = board[i][j]
                if k != ".":
                    k = int(k)
                    if k < 1 and k > 9:
                        return False
                    if k in dic:
                        return False
                    dic.add(k)

            dic.clear()

        for i in range(9):
            for j in range(9):
                k = board[j][i]
                if k != ".":
                    k = int(k)
                    if k < 1 and k > 9:
                        return False
                    if k in dic:
                        return False
                    dic.add(k)

            dic.clear()

        for a in range(3):
            a *= 3
            for b in range(3):
                b *= 3 
                print(a, b)
                for i in range(a, a + 3):
                    for j in range(b, b + 3):
                        k = board[i][j]
                        if k != ".":
                            k = int(k)
                            if k < 1 and k > 9:
                                return False
                            if k in dic:
                                return False
                        dic.add(k)
                        
                dic.clear()

        return True

