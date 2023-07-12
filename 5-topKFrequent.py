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