from . import stocks_blueprint
from flask import render_template, request, session, redirect, url_for, flash, current_app


@stocks_blueprint.before_request
def stocks_before_request():
    current_app.logger.info('Calling before_request() for the stocks blueprint...')


@stocks_blueprint.after_request
def stocks_after_request(response):
    current_app.logger.info('Calling after_request() for the stocks blueprint...')
    return response


@stocks_blueprint.teardown_request
def stocks_teardown_request(error=None):
    current_app.logger.info('Calling teardown_request() for the stocks blueprint...')

@stocks_blueprint.route('/',methods=['GET'])
def index():
    current_app.logger.info('Calling the index() function.')
    return render_template('stocks/index.html')

@stocks_blueprint.route('/add_stock', methods=['GET', 'POST'])
def add_stock():
    if request.method == 'POST':
        session['stock_symbol'] = request.form['stock_symbol']
        session['number_of_shares'] = request.form['number_of_shares']
        session['purchase_price'] = request.form['purchase_price']
        flash(f"Added new stock ({ request.form['stock_symbol'] }", 'success')
        current_app.logger.info(f"Added new stock ({ request.form['stock_symbol'] })!")
        return redirect(url_for('stocks.list_stocks'))
    else:
        return render_template('stocks/add_stock.html')

@stocks_blueprint.route('/stocks/')
def list_stocks():
    return render_template('stocks/stocks.html')