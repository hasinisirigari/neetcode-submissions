class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict={}
        tdict={}
        for char in s:
            if char in sdict:
                sdict[char]+=1
            else:
                sdict[char]=1
        for let in t:
            if let in tdict:
                tdict[let]+=1
            else:
                tdict[let]=1
        return sdict==tdict
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # s_dict={}
        # t_dict={}
        # for i in s:
        #     if i in s_dict:
        #         s_dict[i]+=1
        #     else:
        #         s_dict[i]=1
        # for j in t:
        #     if j in t_dict:
        #         t_dict[j]+=1
        #     else:
        #         t_dict[j]=1
        # return s_dict==t_dict
            