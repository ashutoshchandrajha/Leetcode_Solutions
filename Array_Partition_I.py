class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = sorted(nums)
        result = 0
        i=0
        while i<len(l):
            result += l[i]
            i+=2
        return result
        
