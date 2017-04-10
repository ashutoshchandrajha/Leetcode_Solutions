class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = [0]*len(nums)
        r = []
        for i in nums:
            l[i-1] = 1
        for i in range(len(l)):
            if l[i]==0:
                r.append(i+1)
        return r

    
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        r = []
        for i in nums:
            if nums[abs(i)-1]>0:
                nums[abs(i)-1] = nums[abs(i)-1]*-1
        for i in range(len(nums)):
            if nums[i]>0:
                r.append(i+1)
        return r
