class Solution:
    def countOdds(self, low: int, high: int):
        self.low = low
        self.high = high
        return(((high+1)//2) - (low//2))