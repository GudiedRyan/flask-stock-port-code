"""
This file contains functional tests for app.py
"""
import pytest
from app import app

def test_get_add_stock_page():
    """
    GIVEN a Flask application
    WHEN the '/add_stock' page is requested (GET)
    THEN check the response is valid
    """
    with app.test_client() as client:
        response = client.get('/add_stock')
        assert response.status_code == 200
        assert b'Flask Stock Portfolio App' in response.data
        assert b'Add a Stock:' in response.data
        assert b'Stock Symbol (<i>required</i>):' in response.data #works
        assert b'Number of Shares (required):' in response.data #Would fail if I had the <i> tags surrounding required in the template
        assert b'Purchase Price (required) ($):' in response.data
        # This breaks when I keep the <i> or <emph> brackets in the HTML file.

def test_post_add_stock_page():
    """
    GIVEN a Flask app
    WHEN the '/add_stock' page is posted to (POST)
    THEN check that the user is redirected to the '/list_stocks' page
    """
    with app.test_client() as client:
        response = client.post('/add_stock',
                                data={'stock_symbol': 'GEX',
                                    'number_of_shares': '123',
                                    'purchase_price': '4'},
                                follow_redirects=True)
        assert response.status_code == 200
        assert b'List of Stocks:' in response.data
        assert b'Stock Symbol' in response.data
        assert b'Number of Shares' in response.data
        assert b'Share Price' in response.data
        assert b'GEX' in response.data
        assert b'123' in response.data
        assert b'4' in response.data