from polygon import RESTClient


client = RESTClient(api_key="4pgWU0VnA3pVrog6dpqVnkSz9Y0RWa56")


ticker = "MSFT"

# List Aggregates (Bars)
aggs = []
for a in client.list_aggs(ticker=ticker, multiplier=1, timespan="minute", from_="2023-01-01", to="2023-06-13", limit=50000):
    aggs.append(a)

print(aggs)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print("\n")
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2023-01-04")
for trade in trades:
    print("\n")
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print("\n")
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2023-09-21")
for quote in quotes:
    print("\n")
    print(quote)

