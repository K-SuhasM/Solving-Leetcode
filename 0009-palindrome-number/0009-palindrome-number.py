class Solution:
    def isPalindrome(self, x: int) -> bool:
        num1 = str(x)
        num2 = num1[::-1]
        if (num1 == num2):
            return(True)
        else:
            return(False)