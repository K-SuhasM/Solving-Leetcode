class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        self.nums = nums
        arr = []
        for i in nums:
            c = 0
            for j in nums:
                if j != i and j < i:
                    c += 1
            arr.append(c)
        return(arr)