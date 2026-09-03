class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1= set()
        for num in nums:
            if num in nums1:
                return True
            nums1.add(num)
        return False        
        
        
        
        
        
        
        
        # nums1= set(nums)
        # if sorted(nums)==sorted(nums1):
        #     return False
        # return True
        



























        # nums1=set()
        # for i in nums:
        #     if i in nums1:
        #         return True
        #     else:
        #         nums1.add(i)
        # return False
            