class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        out = []

        for i in range (0, len(nums)):
            if nums[i] % 2 == 0:
                out.insert(0, nums[i])

            if nums[i] % 2 != 0:
                out.append(nums[i])

        return(out)