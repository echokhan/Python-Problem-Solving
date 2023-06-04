#Own solution without Neecode
class Solution1(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diction = {}
        for i in nums:
            if i in diction:
                diction[i] = diction[i] + 1
            else:
                diction[i] = 1
        
        return len([i for i in list(diction.values()) if i != 1]) != 0
		
#Own solution without Neecode, but as per requirement - O(n) Time complexity
class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        diction = {}
        for i in nums:
            if i in diction:
                return True
            else:
                diction[i] = 1
        
        return False
		

#Neecode bruteforce O(n2) time complexity
class Solution3(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i, n in enumerate(nums):
            for j, m in enumerate(nums):
                if n == m:
                    continue
				
                if i == j:
                    return True
		
        return False
		
		
#Own solution with Neecode, but as per requirement - O(n) Time complexity 
#To check for a duplicates, we just needed a data structure that contains unique elements. Dictionary keys are always unique, therefore it was used.
#However, values were redundant and unnecessary
#Thus, we should use a set instead.
class Solution4(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueSet = set()
        for i in nums:
            if i in uniqueSet:
                return True
            else:
                uniqueSet.add(i)
        
        return False
		
		
#A beautiful solution that I saw on leetcode using sets
class Solution5(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        uniqueSet = set(nums)
        if len(uniqueSet) == len(nums):
             return False
        else:
            return True