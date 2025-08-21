from flask import Flask, render_template, request, jsonify, redirect, url_for
import requests
from datetime import datetime
import json
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


API_KEY = os.getenv('API_KEY')
print("Loaded API_KEY:", API_KEY)


POPULAR_STOCKS = {
    'AAPL': 'Apple Inc',
    'MSFT': 'Microsoft Corporation',
    'GOOGL': 'Alphabet Inc (Google)',
    'AMZN': 'Amazon.com Inc',
    'TSLA': 'Tesla Inc',
    'META': 'Meta Platforms Inc',
    'NVDA': 'NVIDIA Corporation',
    'NFLX': 'Netflix Inc'
}


def get_stock_data(symbol):
    url = f"http://api.marketstack.com/v2/eod?access_key={API_KEY}&symbols={symbol}&limit=30"

    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return None


def analyze_stock_data(data):
    if not data or 'data' not in data or not data['data']:
        return None

    stock_data = data['data']
    latest = stock_data[0]  # Most recent day

    current_price = latest['close']
    previous_price = stock_data[1]['close'] if len(stock_data) > 1 else current_price
    daily_change = current_price - previous_price
    daily_change_percent = (daily_change / previous_price) * 100 if previous_price else 0

    week_ago_price = stock_data[5]['close'] if len(stock_data) > 5 else current_price
    weekly_change = current_price - week_ago_price
    weekly_change_percent = (weekly_change / week_ago_price) * 100 if week_ago_price else 0

    avg_volume = sum(day['volume'] for day in stock_data[:5]) / min(5, len(stock_data))
    volume_trend = "High" if latest['volume'] > avg_volume * 1.2 else "Normal" if latest[
                                                                                      'volume'] > avg_volume * 0.8 else "Low"
    recent_prices = [day['close'] for day in stock_data[:5]]
    trend = "Rising" if recent_prices[0] > recent_prices[-1] else "Falling" if recent_prices[0] < recent_prices[
        -1] else "Stable"

    return {
        'symbol': latest['symbol'],
        'company_name': latest['name'],
        'current_price': current_price,
        'daily_change': daily_change,
        'daily_change_percent': daily_change_percent,
        'weekly_change': weekly_change,
        'weekly_change_percent': weekly_change_percent,
        'volume': latest['volume'],
        'volume_trend': volume_trend,
        'price_trend': trend,
        'last_updated': latest['date'],
        'high_52w': max(day['high'] for day in stock_data),
        'low_52w': min(day['low'] for day in stock_data),
        'historical_data': stock_data[:10]
    }


@app.route('/')
def index():
    return render_template('index.html', popular_stocks=POPULAR_STOCKS)


@app.route('/stock/<symbol>')
def stock_detail(symbol):
    data = get_stock_data(symbol.upper())
    if not data:
        return render_template('error.html',
                               message="Could not fetch stock data. Please check the symbol or try again later.")

    analysis = analyze_stock_data(data)
    if not analysis:
        return render_template('error.html', message="No data available for this stock symbol.")

    return render_template('stock_detail.html', stock=analysis)


@app.route('/api/stock/<symbol>')
def api_stock_data(symbol):
    data = get_stock_data(symbol.upper())
    if not data:
        return jsonify({'error': 'Could not fetch stock data'}), 400

    analysis = analyze_stock_data(data)
    if not analysis:
        return jsonify({'error': 'No data available for this stock'}), 400

    return jsonify(analysis)


@app.route('/search', methods=['POST'])
def search_stock():
    symbol = request.form.get('symbol', '').upper().strip()
    if not symbol:
        return render_template('error.html', message="Please enter a stock symbol.")

    return redirect(url_for('stock_detail', symbol=symbol))


if __name__ == '__main__':
    app.run()

