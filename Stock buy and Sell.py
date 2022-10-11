class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for cur_price in prices:
            buy = min(buy,cur_price)
            profit = max(profit, (cur_price - buy))

        return profit
