class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 11000  # generic high num to be overwritten
        max = 0
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            else:
                if prices[i] - min > max:
                    max = prices[i] - min
        return max
