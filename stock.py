import csv
import os

# Sample stock prices(Not live market data)

stock_prices={"AAPL" : 180.00,
              "TSLA" : 250.00,
              "GOOGL": 140.00,
              "MSFT" : 420.00,
              "AMZN" : 190.00,
              "NVDA" : 120.00,
              "META" : 500.00}

def display_stocks():
    print("Available stocks and sample ")
    print("-"*40)
    print(f"{'Symbol':<12}{'Price (USD)':>15}")
    print("-"*40)

    for symbol, price in stock_prices.items():
        print(f"{symbol:<12}${price:>14.2f}")

    print("-"*40)

def get_positive_quantity():
    while True:
        quantity = input("Enter the quantity of shares : ").strip()

        try:
            quantity = int(quantity)

            if quantity <= 0:
                print("Quantity must be greater than 0.")
                continue
            
            return quantity
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def save_portfolio(portfolio, total_investment):
    filename="portfolio.csv"

    try:
        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer= csv.writer(file)

        writer.writerow([
            "Stock Symbol", "Price per Share (USD)", "Quantity", "Investment Value (USD)"
        ])

        for symbol, quantity in portfolio.items():
            price = stock_prices[symbol]
            value = price * quantity

            writer.writerow([
                symbol, f"{price:.2f}",
                quantity,
                f"{value:.2f}"
            ])

        writer.writerow([])
        writer.writerow(["Total Investment (USD)", f"{total_investment:.2f}"])

        print(f"\nPortfolio saved successfully to {os.path.abspath(filename)}")

    except OSError as error:
        print(f"Could not save portfolio: {error}")


def main():
    portfolio = {}

    print("="*50)
    print("Stock Portfolio Tracker")
    print("="*50)
    print("Note: Prices are predefined sample prices, not live market data")

    display_stocks()

    while True:
        symbol = input("\nEnter the stock symbol(or type 'done' to finish) : ").strip().upper()

        if symbol == "DONE":
            break

        if symbol not in stock_prices:
            print("Stock not available. Please choose from the available stocks.")
            continue

        quantity = get_positive_quantity()

        portfolio[symbol] = portfolio.get(symbol,0) + quantity

        print(f"Ädded {quantity} shares of {symbol}. ")

    if not portfolio:
        print("\nNo stocks were added. Portfolio not saved.")
        return

    print("\n" + "="*50)
    print("          Your Portfolio Summary")
    print("="*50)
    print(f"{'Symbol':<12}{'Price':>12}{'Quantity':>12}{'Total Value':>20}")
    print("-"*50)

    total_investment = 0

    for symbol, quantity in portfolio.items():
        price = stock_prices[symbol]
        investment_value = price * quantity
        total_investment += investment_value

        print(f"{symbol:<12}"f"${price:>10.2f}"f"{quantity:>12}"f"${investment_value:>18.2f}")

    print("-"*50)
    print(f"{'TOTAL INVESTMENT':<36}${total_investment:>18.2f}")
    print("="*50)

    save_choice = input("\nSave portfolio to CSV? (yes/no): ").strip().lower()

    if save_choice in ("yes","y"):
        save_portfolio(portfolio, total_investment)
    else:
        print("Portfolio was not saved.")

    print("\nThankyou for using Stack Portfolio Tracker.")


if __name__ == "__main__":
    main()

