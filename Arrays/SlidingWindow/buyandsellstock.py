# BEST TIME TO BUY AND SELL STOCK

'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6)

'''

'''
APPROACH (sliding window):
1. Initialize a min_price to the first element of the index (left pointer)
2. iterate over the prices array: (right pointer)
    2.1 calculate profit as current price - min_price (right pointer - left pointer)
    2.2 if profit greater than existing profit, update
    2.3 if current element smaller than min_price, update (left pointer moves ahead by 1, this is the minimum price now)
3. continue to calcualte updated profits or new min_price.
4. return profit
'''

def maxProfit(self, prices: list[int]) -> int:
    profit=0
    min_price=prices[0] 
    for i in range(1,len(prices)):
        running_profit=prices[i]-min_price
        if(running_profit)>profit:
            profit=running_profit
        if prices[i]<min_price:
            min_price=prices[i]
    return profit


            


        