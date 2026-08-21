## Buy & Sell Stocks 
class Array:
    def buy_sell(self, prices):
        if not prices:
            return 0
            
        max_profit = 0
        best_buy = prices[0]
        for price in prices:
            profit = price - best_buy
            max_profit = max(max_profit, profit)
            best_buy = min(best_buy, price)
        return max_profit

ans = Array()
prices = [7, 1, 5, 3, 6, 4]
print(f"Maximum Profit: {ans.buy_sell(prices)}")