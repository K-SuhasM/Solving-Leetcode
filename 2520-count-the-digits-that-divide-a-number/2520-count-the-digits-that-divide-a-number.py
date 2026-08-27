class Solution:
    def countDigits(self, num: int) -> int:
        nums = str(num)
        c = 0
        for i in nums:
            if num%int(i) == 0:
                c+=1
        return(c)