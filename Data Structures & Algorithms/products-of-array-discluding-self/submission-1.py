class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # final=[]   brute force o(n^2) space=o(n)
        # n=len(nums)
        # for i in range(n):
        #     j=0
        #     res=1
        #     while(j<n):
        #         if(i==j):
        #             j+=1
        #             continue
        #         res*=nums[j]
        #         j+=1
        #     final.append(res)
        # return final

        #optimized approach o(n) and space=o(1)
        n=len(nums)
        final=[1]*n
        #calcuating prefix of each elt i
        prefix=1
        for i in range(0,n):
            final[i]=prefix
            prefix*=nums[i]
        #calcuating postfix of each elt and multiplying with the final array
        postfix=1
        for i in range(n-1,-1,-1):
            final[i]*=postfix
            postfix*=nums[i]
        return final
            
              

            


        