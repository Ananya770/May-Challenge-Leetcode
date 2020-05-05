class Solution:
    def firstUniqChar(self, s: str) -> int:
        char={}
        for i in range(0,len(s)):
            if s[i] in char:
                char[s[i]]=char.get(s[i])+1
            else:
                char[s[i]]=1   
        print(char)             
        
        C=0
        for key,value in char.items():
            if value==1:
                return s.find(key)
            C=C+1

        return -1
R=Solution()     
Result=R.firstUniqChar("dddccdbba")
print(Result)