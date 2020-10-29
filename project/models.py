from project import database

class Stock(database.Model):
    "Class to represent purchased stock in portfolio"

    __tablename__ = 'stocks'

    id = database.Column(database.Integer, primary_key=True)
    stock_symbol = database.Column(database.String, nullable=False)
    number_of_shares = database.Column(database.Integer, nullable=False)
    purchase_price = database.Column(database.Integer, nullable=False)

    def __init__(self, stock_symbol: str, number_of_shares: str, purchase_price: str):
        self.stock_symbol = stock_symbol
        self.number_of_shares = int(number_of_shares)
        self.purchase_price = int(float(purchase_price) * 100)

    def __repr__(self):
        return f'{self.stock_symbol} - {self.number_of_shares} shares purchased at ${self.purchase_price / 100}'