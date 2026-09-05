class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0

        maxs = nums[0]

        for i in range(len(nums)):
            cur += nums[i]
            if cur > maxs:
                maxs = cur
            if cur < 0:
                cur = 0

        return(maxs)
