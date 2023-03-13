
stock_prices = {}
with open("stock_Prices.csv", "r") as f:
    print("hr")
    for line in f:
        tokens = line.split(',')
        day = tokens[0]
        price = float(tokens[1])
        stock_prices[day] = price


print(stock_prices)

print(stock_prices['09-Mar'])
