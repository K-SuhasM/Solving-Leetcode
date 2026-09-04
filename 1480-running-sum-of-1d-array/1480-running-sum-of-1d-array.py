class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        out = []
        out.append(nums[0])
        for i in range(1,len(nums)):
            a = nums[i] + out[i-1]
            out.append(a)
        return(out)