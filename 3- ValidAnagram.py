#Own solution without Neecode
class Solution1(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = list(s)
        t = list(t)

        dictions = {}
        for i in s:
          if i in dictions:
            dictions[i] = dictions[i] + 1
          else:
            dictions[i] = 1

        dictiont = {}
        for i in t:
          if i in dictiont:
            dictiont[i] = dictiont[i] + 1
          else:
            dictiont[i] = 1

        if dictions.keys() != dictiont.keys():
          return False

        for i in s:
          if dictions[i] != dictiont[i]:
            return False

        return True
		
#Own solution with Neecode O(1) space complexity. time complexity depends on sorted
class Solution2(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        return sorted(s) == sorted(t)
		

#Leetcode solution, where rather than dictionary, a combination of string method count() and set is used.
class Solution3(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
          return False

        for i in set(s):
          if s.count(i) != t.count(i):
            return False

        return True