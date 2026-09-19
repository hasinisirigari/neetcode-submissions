class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        numset=set(nums)
        for i in nums:
            if i-1 not in numset:
                length=1
                while i+length in numset:
                    length+=1
                longest=max(length,longest)
        return longest







































        # numset=set(nums)
        # longest=0
        # for num in numset:
        #     if num-1 not in numset:
        #         length=1
        #         while num+length in numset:
        #             length+=1
        #         longest = max(length,longest)
        # return longest

            