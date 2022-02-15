"""
Calcualte max profit that you can have in a single trade

Notes:
* In this example, buy when 1 and sell when 6 for profit of 5
"""

# Input
prices = [7, 1, 5, 3, 6, 4]
output = 5

############ Initial Answer (n) ########
min_price = prices[0]
profit = 0

for price in prices:
    min_price = min(min_price, price)
    profit = max(profit, price - min_price)

print(profit)
#######################################
