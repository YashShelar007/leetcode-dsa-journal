"""
LeetCode Problem: Best Time to Buy and Sell Stock
Category: Greedy
Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Approach: One-pass tracking minimum buy price

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0               # index of the lowest price seen so far (buy day)
        maxProfit = 0       # best profit we can make

        for i in range(len(prices)):
            # potential profit if we sold today
            profit = prices[i] - prices[l]

            # if today’s price is even lower, update buy day
            if prices[i] < prices[l]:
                l = i

            # keep the best profit
            if profit > maxProfit:
                maxProfit = profit
        
        return maxProfit
