class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        profit = 0
        CanSell = False
        for i in range(N):
            if i == N-1:
                if CanSell:
                    profit += prices[i]
            elif(prices[i] < prices[i+1] and not CanSell):
                profit -= prices[i]
                CanSell = not CanSell
            elif prices[i] > prices[i+1] and CanSell:
                profit += prices[i]
                CanSell = not CanSell

        return profit



