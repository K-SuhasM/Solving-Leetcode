class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []

        for i in range(1,len(nums)+1):
            a = sum(nums[0:i])
            out.append(a)
        return(out)