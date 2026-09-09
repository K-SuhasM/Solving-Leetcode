class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}

        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] += 1

        for j in s:
            if dict1[j] == 1:
                return s.index(j)
                break
        return -1
