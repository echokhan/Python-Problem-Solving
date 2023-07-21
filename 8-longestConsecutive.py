#Own solution, without neetcode or leetcode
#First wrote solution, then did changed solution as per test cases that failed
class Solution1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from collections import defaultdict
        #nums = [100,4,200,1,3,2]
        #nums = [0,3,7,2,5,8,4,6,0,1]
        #Sort to tread the list and avoid duplication (want consecutive element sequences)
        sorted_nums = sorted(list(set(nums)))
        print(sorted_nums)
        seq = defaultdict(list)
        #Used to have a variable to store when a new subsequence starts
        speedbreaker = 0
        for i, j in enumerate(sorted_nums):
          #print(i,j)
          #print(seq)
          if i != 0:
            #This is when we have reached the end of sorted_nums, but have consecutive elements since last speedbreaker
            if i == len(sorted_nums) - 1 and j - sorted_nums[i-1] == 1:
              subsequence = sorted_nums[speedbreaker:]
              seq[len(subsequence)] = subsequence
              continue
            #Anywhere when treading the list, if difference with previous element is more than 1, then subsequence has ended and new speedbreaker assigned (to indicate start of new subsequence)
            if j - sorted_nums[i-1] > 1:
              subsequence = sorted_nums[speedbreaker:i]
              seq[len(subsequence)] = subsequence 
              speedbreaker = i

        if bool(seq):
          print(seq)
          return sorted(seq.keys(), reverse=True)[0]
        #In case the entire sorted list is a subsequence
        else:
          return len(set(sorted_nums))