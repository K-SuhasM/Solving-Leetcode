class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxi = max(candies)
        out = []
        for i in candies:
            out.append((i+extraCandies)>=maxi)
        return(out)