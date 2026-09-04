class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for num in nums:
            if num in res:
                res[num]+=1
            else:
                res[num]=1
        keys = sorted(res, key=res.get, reverse=True)
        return keys[:k]

 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
        # res={}
        # for i in nums:
        #     if i in res:
        #         res[i]+=1
        #     else:
        #         res[i]=1
        # desc= dict(sorted(res.items(), key=lambda item: item[1], reverse=True))
        # keys=list(desc.keys())
        # return keys[:k]
