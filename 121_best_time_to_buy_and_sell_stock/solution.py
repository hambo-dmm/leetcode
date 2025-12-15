    from typing import List

    class Solution:
        def maxProfit(self, prices: List[int]) -> int:
            if not prices:
                return 0

            lowest_buy = prices[0]
            max_profit = 0

            for i in range(1, len(prices)):
                max_profit = max(max_profit, prices[i] - lowest_buy)
                lowest_buy = min(prices[i], lowest_buy)

            return max_profit