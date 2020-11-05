import pytest
from project.models import Stock, User

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

def test_new_user(new_user):
    """
    GIVEN a User model
    WHEN a new User obj is created
    THEN check the email is valid and hashed password is not the same as the password entered
    """
    assert new_user.email == 'obamium@email.com'
    assert new_user.password_hashed != 'GexIsTheBest431'
