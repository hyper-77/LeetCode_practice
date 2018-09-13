class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in hash:
                return[hash[compl],i]
            else:
                hash.setdefault(nums[i],i)