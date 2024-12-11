class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1 #l is buying and r is selling
        maxP=0
        while r<len(prices):
            #Profitable
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxP=max(maxP,profit)
            else:
                l=r
            r+=1
        return maxP
