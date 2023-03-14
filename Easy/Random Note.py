class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #see if you can write ransomnote from only the characters exist in the magazine. can only use the char once. if use it only once, all the characters in ransomenote should exist in the magazine. So show if all the characters exist in the magazine. Use the simple for each loop

        #or...count all the characters in ransome and count all characters in magazine and if the numbers do not match return false, also if the character in ransome don't exist in maga, return false. if number of char is bigger in maga, that means you can use the char to make ransom. If there is not enough char, which means numb of char is bigger in ransom, we cannot make it.
        ransom = {}
        maga = {}
        for cha in ransomNote:
            if cha not in ransom:
                ransom[cha] = 1
            else:
                ransom[cha] += 1
        
        for cha in magazine:
            if cha not in maga:
                maga[cha] = 1
            else:
                maga[cha] += 1

        print(maga)

        for key in ransom:
            if key not in maga:
                return False
            else:
                if ransom[key] > maga[key]:
                    return False

        return True