#Own solution
class Solution1(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        collect_dict = defaultdict(int)
        for i in nums:
          collect_dict[i] += 1
        print(collect_dict)
        
        key_list = collect_dict.keys()
        frequency_list = collect_dict.values()
        return [i[0] for i in sorted(list(zip(key_list, frequency_list)), key=lambda x:x[1],reverse=True)[:k]]

#My interpretation of neetcode's explaination
class Solution2(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        #frequency dictionary to be later used for finding frequency of elements in nums
        frequency_dict = {}
        #count_array of size of maximum possible frequency (length of nums) (if list is of size 6, any number could only be repeated   
        #maximum 6 times)
        #each element is a bucket or sublist to cater for collision
        #collision is where one or more elements has same frequency
        #without buckets/sublists, they might be overwritten on the same position or index in count_array
        count_array = [[] for i in range(len(nums) + 1)]

        #adding frequency of each element as value and element as key, to dictionary
        for i in nums:
          if i in frequency_dict.keys():
            frequency_dict[i] += 1
          else:
            frequency_dict[i] = 1
        
        #adding elements in count_array, on index which is same as frequency of element
        for i, j in frequency_dict.items():
          count_array[j].append(i)
          

        topK = []
        #iterating count_array in descending order, skipping empty buckets/sublists
        for i in count_array[::-1]:
          if i:
            topK.append(i)
            print(i)

        #flattening final list and returning topk elements from list
        return sum(topK, [])[:k]