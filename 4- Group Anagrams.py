from collections import defaultdict

def isAnagram(s, t):
  if len(set(s)) != len(set(t)):
    return False
  else:
    for i in s:
      if s.count(i) != t.count(i):
        return False
    return True

#Own solution after hit and trial.
#Passed 111/118 test cases before a time limit error
#Unoptimized
class Solution1(object):
  def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict = {}
        for s in strs:
          if s not in strs_dict.keys():
            anagramFound = False
            for t in [t for t in strs_dict.keys() if t != s]:
              anagramFound = isAnagram(s, t)
              if anagramFound:
                  if t in strs_dict.keys():
                    strs_dict[t].append(s)
                    break
              else:
                continue
            if anagramFound == False:
              strs_dict[s] = []
              strs_dict[s].append(s)
          else:
            strs_dict[s].append(s)

        return list(strs_dict.values())

#A solution I found on leetcode. Intiailised a dictionary with default value type: list. Also, created keys from sorted elements.
class Solution2(object):
  def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        strs_dict = defaultdict(list)
        for i in strs:
          str_key = tuple(sorted(i))
          strs_dict[str_key].append(i)

        final_list = []
        for i in strs_dict.values():
          final_list.append(i)
        return final_list
  
  #Neetcode solution. Was supposed to have a faster runtime. It is fast, but slower than above, timesort solution.
  class Solution3(object):
    def groupAnagrams(self, strs):
          """
          :type strs: List[str]
          :rtype: List[List[str]]
          """
          strs_dict = defaultdict(list)
          for i in strs:
              unicode_list = [0] * 26
              for str in i:
                  unicode_list[ord(str) - ord('a')] +=1

              str_key = tuple(unicode_list)
              strs_dict[str_key].append(i)

          final_list = []
          for i in strs_dict.values():
            final_list.append(i)
          return final_list