class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = {}
        r = []
        for i in range(len(nums)):
            if nums[i] not in d:
                d[nums[i]]=i
        print(d)
        for i in range(len(nums)):
            if target-nums[i] in d and d[target-nums[i]]!=i:
                return [d[target-nums[i]],i]
        return []
