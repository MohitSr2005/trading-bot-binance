**Binance Futures Testnet Trading Bot**
A simple, structured Python-based CLI trading bot that interacts with Binance Futures Testnet (USDT-M).
This project demonstrates API integration, order execution, validation, logging, and clean code practices.

**Features**
* Place **MARKET** and **LIMIT** orders
* Supports both **BUY** and **SELL**
* CLI-based input using `argparse`
* Input validation (symbol, side, type, quantity, price)
* Smart price validation using real-time market price
* Structured code (modular design)
* Logging of requests, responses, and errors
* Error handling for API & user inputs

**Project Structure**

trading_bot/
│
├── bot/
│   ├── client.py          # Binance API client setup
│   ├── orders.py          # Order execution logic
│   ├── validators.py      # Input validation
│   ├── logging_config.py  # Logging setup
│   └── __init__.py
│
├── cli.py                 # CLI entry point
├── test_connection.py     # API connection test
├── requirements.txt
├── README.md
└── .env                   # API keys (not committed)

**Setup Instructions**

*1. Clone the repository*
git clone <your_repo_link>
cd trading_bot

*2. Install dependencies*

pip install -r requirements.txt

*3. Create `.env` file*

API_KEY=your_binance_testnet_api_key
API_SECRET=your_binance_testnet_secret_key

Use **Binance Futures Testnet**
https://testnet.binancefuture.com

**Environment Setup**

Create a .env file in the root directory and add your Binance Testnet API credentials:
API_KEY=your_api_key
API_SECRET=your_api_secret

**Usage**

*MARKET Order*
py cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001

*LIMIT Order*

py cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 78000

**Output Example**

Order Summary:
{'symbol': 'BTCUSDT', 'side': 'BUY', 'type': 'MARKET', 'quantity': 0.001}

✅ Order Success!
Order ID: 12345678
Status: FILLED
Executed Qty: 0.001

**Smart Validation**

The bot includes custom validation logic:

* Prevents invalid LIMIT orders before API call
* Uses real-time market price
* Ensures:

  * SELL ≥ market price
  * BUY ≤ market price

**Logging**
All API interactions are logged in:
bot.log
Includes:
* Order request
* Order response
* Errors

**Assumptions**
* Only **USDT-M Futures** supported
* Uses Binance Futures Testnet
* Basic validation implemented (extendable)

**Future Improvements**

* Add Stop-Loss / Take-Profit orders
* Add GUI or Web Interface
* Add automated trading strategies
* Add portfolio tracking

**Author**

Mohit Srivastava

**Notes**
* `.env` file is excluded for security
* API keys should never be shared publicly
* Designed for learning and evaluation purposes
