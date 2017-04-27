class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        n = sorted(nums)[::-1]
        for i in range(len(nums)):
            pos = n.index(nums[i])+1
            if pos<=3:
                nums[i]=medal[pos-1]
            else:
                nums[i]=str(pos)
        return nums
        
