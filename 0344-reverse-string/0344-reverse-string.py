class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
     
        ans = []

        for i in range(1,len(s)+1):
            ans.append(s[-i])

        s.clear()
        s.extend(ans)
        