class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        prev={}
        for i,n in enumerate(nums):
            
            diff=target-n
            if diff in prev:
                return [prev[diff],i]
            prev[n]=i
        return []
                    