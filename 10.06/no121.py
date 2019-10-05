from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n<1: return 0
        min_price = prices[0]
        max_profit = 0
        for i in range(1,n):
            min_price = min(min_price,prices[i])
            max_profit= max(max_profit,prices[i]-min_price)
        return max_profit


if __name__=='__main__':
    s=Solution()
    prices = [7,1,5,3,6,4]
    print(s.maxProfit(prices))