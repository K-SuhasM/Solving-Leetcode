class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0
        mul = 1

        while n>0:
            a=n%10
            sum+=a
            mul*=a
            n = n//10
        return(mul-sum)    
        