class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return None
        self.nums = nums
        self.sums = [0]*len(nums)
        self.sums[0]=self.nums[0]
        for i in range(1,len(nums)):
            self.sums[i] = self.sums[i-1]+nums[i]
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i == 0:
            return self.sums[j]
        return self.sums[j]-self.sums[i-1]
