class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            k = (s[i:i+3])
            if len(k)<3:
                break
            if k[0]!=k[1] and k[1]!=k[2] and k[0]!=k[2] :
                count+=1
        return (count)
        