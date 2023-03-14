class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        #find the frequencies of all the characters in the string and store them in dictionary.
        #iterate through the dictionary, and find the character that has the frequency of one.
        #iterate through the string again and return the first index that you see the character.

        #or...keep track of the character in the string, and if there exist one already, remove that from the cadidate of being our target. After the process of elinimation, we should get the char that appears only once in the string. return the first char in the string.
        seen = ""
        candidates = []
        for cha in s:
            if cha not in seen:
                seen += cha
                candidates.append(cha)
            else:
                if cha in candidates:
                    candidates.remove(cha)
        if candidates == []:
            return -1
        return s.find(candidates[0])
        