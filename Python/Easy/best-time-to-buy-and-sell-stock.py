# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Solution

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0

        minPrices = [prices[0]]
        profit = 0

        for id in range(1,len(prices)):
            if prices[id] < minPrices[id-1]:
                minPrices.append(prices[id])
            else:
                minPrices.append(minPrices[id-1])

            profit = max(profit, prices[id] - minPrices[id])

        return profit