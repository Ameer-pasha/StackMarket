# 🚀 StackMarket  
A Flask-based web application that allows users to fetch and explore **real-time stock market data** using an external API.  

## ✨ Features  
- 📊 Search for stock information by symbol.  
- 📈 View real-time stock details (price, open, high, low, etc.).  
- ⚡ Fast and lightweight Flask backend.  
- 🎨 Simple, responsive UI built with Jinja templates.  

## 🛠️ Installation  
1. Clone the repository:  
   git clone https://github.com/Ameer-pasha/StackMarket.git  
   cd StackMarket  

2. Create a virtual environment:  
   python -m venv venv  
   venv\Scripts\activate   # On Windows  
   source venv/bin/activate # On Mac/Linux  

3. Install dependencies:  
   pip install -r requirements.txt  

4. Configure environment variables:  
   Copy `.env.example` to `.env`.  
   Add your API key inside `.env`:  
   API_KEY=your_api_key_here  

5. Run the Flask server:  
   python main.py  

6. Open in browser:  
   http://127.0.0.1:5000  

## 🎮 Usage  
- Enter a stock ticker (e.g., `AAPL`, `TSLA`, `MSFT`) in the search box.  
- Get real-time stock details displayed instantly.  
- Navigate to stock detail pages for more info.  

## 📂 Project Structure  
StackMarket/  
│── main.py              # Flask application  
│── .env.example         # Example environment variables  
│── .gitignore  
│── templates/           # HTML templates  
│    ├── base.html  
│    ├── index.html  
│    ├── stock_detail.html  
│    └── error.html  

## ⚙️ Tech Stack  
- **Backend**: Flask (Python)  
- **Frontend**: HTML, Jinja2  
- **API**: Stock Market API (via API key)  

## 📌 Future Improvements  
- 🔎 Add historical stock data & charts.  
- 💾 Database integration for saving searches.  
- 🌐 User authentication for personalized watchlists.  

## 👤 Author  
**Ameer Pasha**  
🔗 [GitHub Profile](https://github.com/Ameer-pasha)  
