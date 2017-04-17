class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sum = 0
        max = float("-inf")
        for i in nums:
            sum = sum + i+1
            if i+1 > max:
                max = i+1
        if sum == (max*(max+1))/2:
            return max
        else:
            return (max*(max+1))/2 - sum - 1
