class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        num = str(n)
        pro = 1
        sum = 0
        for i in num:
            pro*=int(i)

        for j in num:
            sum+=int(j)
        return(pro-sum)