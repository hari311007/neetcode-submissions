class Solution:
   
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen=set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
#approach 2:
#sort the array and compare nums[i]==nums[i-1] where loop is #from 1 to n
#approach 3(brute force):
#for i in range(len(nums)):
#    for j in range((len(nums))):
#        if nums[i]==nums[j]:
#         return true

      


        
        