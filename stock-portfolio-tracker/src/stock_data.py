class StockData:
    def __init__(self):
        self.prices = {
            "AAPL": 180,
            "TSLA": 250,
            "GOOGL": 2800,
            "MSFT": 320,
            "AMZN": 3400
        }

    def get_price(self, symbol):
        symbol = symbol.upper()

        if symbol not in self.prices:
            raise KeyError(f"Stock '{symbol}' not found")

        return self.prices[symbol]
