class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        listi=[]
        for i in range(0,len(nums)):
            for j in range(1,len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target and len(listi)!=2:
                        listi.append(i)
                        listi.append(j)

        return listi