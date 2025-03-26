from typing import List, Optional

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0
    
    min = prices[0]
    max_profit = 0

    for i in range(1, len(prices)):
        if prices[i] < min:
            min = prices[i]
        else:
            max_profit = max(prices[i] - min, max_profit)

    return max_profit

print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))