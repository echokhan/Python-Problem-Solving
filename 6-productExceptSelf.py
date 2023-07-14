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
