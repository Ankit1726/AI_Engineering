## Buy & Sell Stock 

class Solution:
     def stock(self,prices): # TC:O(n)
          n = len(prices)
          max_profit = 0
          min_price = float("inf")

          for i in range(n):
               # track minimum price  of stock
               min_price = min(min_price,prices[i])
               profit = prices[i] - min_price 
               max_profit = max(max_profit,profit)

          return max_profit

prices = [7,2,1,5,6,4,8]
sol = Solution()
ans = sol.stock(prices)
print(f"Maximum Profit To Sell Stock: {ans}")
               