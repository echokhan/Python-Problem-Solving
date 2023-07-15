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

#Prefix, suffix lists/arrays used to find prefix product and suffix product
class Solution3(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)

        if length == 1:
          return [0]

        #list to find cumulative product from left side of nums[i]
        left_pass = [1] * length
        print("Initial left_pass")

        #list to find cumulative product from right side of nums[i]
        right_pass = [1] * length

        #Finding product for each nums[i] of left side elements (left to right)
        for i in range(1, length):
          left_pass[i] = left_pass[i-1] * nums[i -1]
        print("Processed left_pass", left_pass)

        #Finding product for each nums[i] of right side elements (right to left)
        for i in range(length - 2, -1, -1):
          right_pass[i] = right_pass[i+1] * nums[i+1]
        print("Processed right_pass", right_pass)

        return [left_pass[i] * right_pass[i] for i in range(length)]