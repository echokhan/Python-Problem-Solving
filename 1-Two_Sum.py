class Solution1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    return [i, j]


