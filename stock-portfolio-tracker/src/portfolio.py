from stock_data import StockData


class Portfolio:
    def __init__(self):
        self.stock_data = StockData()
        self.holdings = {}

    def add_stock(self, symbol, quantity):
        symbol = symbol.upper()

        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity

    def calculate_total(self):
        total = 0

        for symbol, qty in self.holdings.items():
            price = self.stock_data.get_price(symbol)
            total += price * qty

        return total

    def summary(self):
        result = []

        for symbol, qty in self.holdings.items():
            price = self.stock_data.get_price(symbol)

            result.append({
                "symbol": symbol,
                "quantity": qty,
                "price": price,
                "value": price * qty
            })

        return result
