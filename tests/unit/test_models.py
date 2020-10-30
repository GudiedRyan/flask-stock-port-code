import pytest
from project.models import Stock

@pytest.fixture(scope='module')
def new_stock():
    stock = Stock('GEX', '16', '406.78')
    return stock

def test_new_stock(new_stock):
    """
    GIVEN a Stock model
    WHEN a new Stock object is created
    THEN check the symbol, number of shares, and purchase price fields are defined correctly
    """
    stock = Stock('GEX', '16', '406.78')
    assert stock.stock_symbol == 'GEX'
    assert stock.number_of_shares == 16
    assert stock.purchase_price == 40678