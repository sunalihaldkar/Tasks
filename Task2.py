def stock_portfolio():
    prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 2700, "MSFT": 300, "AMZN": 3300}
    total = 0

    print("Enter stock details (type 'done' to finish):")
    while True:
        stock = input("Stock symbol: ").upper()
        if stock == "DONE":
            break
        if stock in prices:
            qty = int(input(f"Quantity of {stock}: "))
            total += prices[stock] * qty
        else:
            print("Stock not found in database.")

    print(f"\nTotal Investment: ${total}")

stock_portfolio()
