class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        #r = 0 #index in randonNote
        m = 0 #index in magazine
        mlist = [0]*len(magazine)
        count = 0
        for r in range(len(ransomNote)):
            m = 0
            while m<len(magazine):
                if ransomNote[r]==magazine[m] and mlist[m]!=1:
                    mlist[m] = 1
                    count += 1
                    break
                m += 1
        print(count)
        if count == len(ransomNote):
            return True
        else:
            return False


obj = Solution()
print(obj.canConstruct("bg","efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"))
