class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]
        sum = nums[0]
        maxs = nums[0]
        for i in range(1,len(nums)):
            sum = max(sum+nums[i],nums[i])
            maxs = max(sum, maxs)
        return maxs
