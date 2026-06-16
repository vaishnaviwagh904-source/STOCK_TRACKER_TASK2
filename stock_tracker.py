stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330
}

total_value = 0
report = ""

print("Available Stocks:")
for stock, price in stock_prices.items():
    print(stock, ":", price)

while True:
    stock = input("\nEnter Stock Name (or 'done'): ").upper()

    if stock == "DONE":
        break

    if stock in stock_prices:
        qty = int(input("Enter Quantity: "))
        value = stock_prices[stock] * qty
        total_value += value

        report += f"{stock} - {qty} shares = ${value}\n"
    else:
        print("Invalid Stock!")

report += f"\nTotal Investment Value = ${total_value}"

print("\n", report)

with open("portfolio_report.txt", "w") as file:
    file.write(report)

print("Report Saved Successfully!")