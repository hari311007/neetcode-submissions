from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_freq=defaultdict(int)

        for i in nums:
            hash_freq[i]+=1
        sorted_key=sorted(hash_freq.items(),key=lambda x :x[1],reverse=True)
        return [item[0] for item in sorted_key][:k]