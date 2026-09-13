class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()
        for i,num in enumerate(nums):
            if num>0:
                break
            if i>0 and num==nums[i-1]:
                continue
            l,r=i+1,len(nums)-1
            while l<r:
                total = num+nums[l]+nums[r]
                if total==0:
                    res.append([num,nums[l],nums[r]])
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return res






















            # j=i+1
            # k=len(nums1)-1
            # tot=nums[j]+nums[k]+num
            # if tot==0:
            #     res.append([num,nums[j],nums[k]])
            # elif tot<0:
            #     j+=1
            # else:
            #     k-=1
