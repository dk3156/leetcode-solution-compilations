class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dic = {}
        for elem in s:
            if elem not in s_dic:
                s_dic[elem] = 1
            else:
                s_dic[elem] += 1
        for elem in t:
            if elem not in s_dic:
                return False
            else:
                s_dic[elem] -= 1
        for elem in s:
            if s_dic[elem] != 0:
                return False
        
        return True
        