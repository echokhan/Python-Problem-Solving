from operator import mul
from functools import reduce        
        
#Own solution
#Created a dictionary, with values as products of other elements
#The requirement was that of O(n), and below solution gives O(n2)
#Failed with time limit exceed after passing 18 / 22 testcases
class Solution1(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = {}
        for i, j in enumerate(nums):
          lst = [m for n, m in enumerate(nums) if n != i]
          if lst is None:
            lst = [0]
          product[i] = reduce(mul, lst)

        return list(product.values())

#Own solution
#Tried to use conditions to find products depending on position
#Unfortunately, still unoptimized
#The requirement was that of O(n), and below solution gives O(n2)
#Failed with time limit exceed after passing 18 / 22 testcases
class Solution2(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for i, j in enumerate(nums):
            if i == 0:  answer.append(reduce(lambda x, y: x*y, (nums[1:])))
            elif i == len(nums) - 1:  answer.append(reduce(lambda x, y: x*y, nums[:len(nums) - 1]))
            else:  answer.append(reduce(lambda x, y: x*y, (nums[:i] + nums[i+1:])))
        return answer
