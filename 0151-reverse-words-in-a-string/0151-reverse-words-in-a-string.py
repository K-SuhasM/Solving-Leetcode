class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split()
        out = []
        str = ""

        for i in range(1, len(s)+1):
            out.append(s[-i])

        for i in out:
            str+= f" {i}"

        return(str.strip())