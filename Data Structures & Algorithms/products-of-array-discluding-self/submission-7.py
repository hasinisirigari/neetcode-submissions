class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]
        postfix=1
        for i in range (len(nums)-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res




























        # result = []
        # for i in range(len(nums)):
        #     nums1= nums[:i]+nums[i+1:]
        #     prod = 1
        #     for j in range(len(nums1)):
        #         prod*=nums1[j]
        #     result.append(prod)

        # return result
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
      
        # result=[]
        # for i in range (len(nums)):
        #     nums1=nums[:i]+nums[i+1:]
        #     prod=1
        #     for j in range (len(nums1)):
        #         prod*=nums1[j]
        #     result.append(prod)
        # return result