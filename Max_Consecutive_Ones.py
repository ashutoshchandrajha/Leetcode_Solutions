class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr = 0    
        max_1 = 0
        for i in nums:
            if i == 1:
                curr+=1
            else:
                curr = 0
            max_1 = max(curr,max_1)
        return max_1
