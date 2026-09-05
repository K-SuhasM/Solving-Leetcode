class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        out = []

        for i in nums:
            out.insert(0, i) if i % 2 == 0 else out.append(i)

        return(out)