# 📈 Stock Dashboard Flask App

A beginner-friendly web application to explore and learn about stock market data using real-time APIs. Perfect for those new to stocks who want to understand what all the numbers mean!

## ✨ Features

- **🔍 Stock Search**: Look up any stock by symbol (AAPL, GOOGL, etc.)
- **📊 Real-time Data**: Current prices, daily changes, and trading volume
- **📈 Trend Analysis**: See if stocks are rising, falling, or stable
- **🎯 Popular Stocks**: Quick access to major companies
- **📚 Educational**: Clear explanations of stock terms and concepts
- **📱 Responsive**: Works on desktop and mobile devices
- **🔗 REST API**: JSON endpoints for developers

## 🚀 Quick Start

### Prerequisites

- Python 3.7+
- Marketstack API key (free at [marketstack.com](https://marketstack.com))

### Installation

1. **Clone or download the project**
```bash
git clone <your-repo-url>
cd stock-dashboard
```

2. **Install required packages**
```bash
pip install flask requests python-dotenv
```

3. **Set up your API key**
   
   Create a `.env` file in the project root:
```env
API_KEY=your_marketstack_api_key_here
```

4. **Create the templates folder structure**
```
your-project/
├── app.py
├── .env
├── requirements.txt
└── templates/
    ├── index.html
    ├── stock_detail.html
    └── error.html
```

5. **Run the application**
```bash
python app.py
```

6. **Open your browser** to `http://localhost:5000`

## 📁 Project Structure

```
stock-dashboard/
├── app.py              # Main Flask application
├── .env                # Environment variables (API key)
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/         # HTML templates
    ├── index.html     # Homepage with stock search
    ├── stock_detail.html  # Individual stock information
    └── error.html     # Error page
```

## 🔑 Getting Your API Key

1. Visit [Marketstack](https://marketstack.com)
2. Sign up for a free account
3. Get your API access key from the dashboard
4. Add it to your `.env` file

**Free tier includes**: 1,000 API calls per month

## 🌟 How to Use

### Web Interface

1. **Homepage**: Browse popular stocks or search for any company
2. **Stock Details**: Click on any stock to see:
   - Current price and daily changes
   - Weekly performance
   - Trading volume and trends
   - Price history table
   - Easy explanations of what everything means

### API Endpoints

- `GET /api/stock/<symbol>` - Returns JSON data for any stock

Example:
```bash
curl http://localhost:5000/api/stock/AAPL
```

Response:
```json
{
  "symbol": "AAPL",
  "company_name": "Apple Inc",
  "current_price": 226.01,
  "daily_change": -3.97,
  "daily_change_percent": -1.72,
  "volume_trend": "High",
  "price_trend": "Falling"
}
```

## 🛠 Dependencies

Create a `requirements.txt` file:
```txt
Flask==2.3.3
requests==2.31.0
python-dotenv==1.0.0
```

Install with: `pip install -r requirements.txt`

## 🎨 What You'll Learn

This app teaches stock market basics:

- **Stock Prices**: What they represent and why they change
- **Daily Changes**: Green (up) vs Red (down) movements
- **Trading Volume**: How many shares are being traded
- **Market Trends**: Whether stocks are generally rising or falling
- **OHLC Data**: Open, High, Low, Close prices

## 🔧 Customization Ideas

Want to extend the app? Try adding:

- **Stock Comparison**: Compare two stocks side by side
- **Watchlist**: Save favorite stocks to track
- **Price Alerts**: Email notifications for price changes  
- **Charts**: Visual graphs using Chart.js or similar
- **News Integration**: Fetch recent stock news
- **Portfolio Tracker**: Track multiple stock investments

## ⚠ Troubleshooting

**Common Issues:**

1. **"Could not fetch stock data"**
   - Check your API key in `.env`
   - Verify you haven't exceeded API limits
   - Ensure stock symbol is valid (e.g., AAPL not Apple)

2. **"No module named 'dotenv'"**
   ```bash
   pip install python-dotenv
   ```

3. **Template not found errors**
   - Ensure `templates/` folder exists
   - Check that HTML files are in the templates directory

## 📊 API Rate Limits

**Free Marketstack Plan:**
- 1,000 requests/month
- Historical data available
- No real-time data (15-20 minute delay)

For production apps, consider upgrading to a paid plan.

## 🤝 Contributing

Want to improve the app?

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙋‍♂️ Need Help?

- Check the [Marketstack API documentation](https://marketstack.com/documentation)
- Review Flask documentation at [flask.palletsprojects.com](https://flask.palletsprojects.com)
- Open an issue if you find bugs or have questions

---

**Happy coding! 🚀** This app is perfect for learning both Flask development and stock market basics.
