def calculate_investment():

  stock_ticker = input("Enter the stock ticker symbol (e.g., MSFT for Microsoft): ")
  num_shares = int(input("Enter the number of shares: "))
  cost_per_share = float(input("Enter the cost per share: "))


  total_investment = num_shares * cost_per_share


  print(f"Stock Ticker Symbol: {stock_ticker}")
  print(f"Number of Shares: {num_shares}")
  print(f"Cost per Share: ${cost_per_share:.2f}")
  print(f"Total Amount Invested: ${total_investment:.2f}")


calculate_investment()