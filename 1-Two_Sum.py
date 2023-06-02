#Unoptimized o(n2)
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


#Optimized o(n)
class Solution2(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        diction = {}
        for i, n in enumerate(nums):
          if target - n in diction:
            return [diction[target-n], i]
          diction[n] = i