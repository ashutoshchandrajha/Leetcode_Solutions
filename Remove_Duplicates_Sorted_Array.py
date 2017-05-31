class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==0 or len(nums)==1:
            return len(nums)
        curr = 0
        for i in range(1,len(nums)):
            if nums[curr]!=nums[i]:
                curr+=1
                nums[curr],nums[i]=nums[i],nums[curr]
        return curr+1
