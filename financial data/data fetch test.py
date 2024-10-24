import yfinance as yf
import numpy as np
import pandas as pd

def fetch_stock_data(symbol : str, start_date : str, end_date : str) -> pd.DataFrame:
    """
    Fetch historical stock data using yfinance.

    Args:
    symbol (str): Ticker symbol of the stock.
    start_date (str): Start date in 'YYYY-MM-DD' format.
    end_date (str): End date in 'YYYY-MM-DD' format.

    Returns:
    pandas.DataFrame: Historical stock data.
    """
    stock_data = yf.download(symbol, start=start_date, end=end_date)
    return stock_data

def preprocess_data(stock_data : pd.DataFrame) -> pd.DataFrame:
    """
    Preprocess historical stock data.

    Args:
    stock_data (pandas.DataFrame): Historical stock data.

    Returns:
    pandas.DataFrame: Preprocessed data.
    """
    # Feature engineering
    stock_data['Daily Return'] = stock_data['Adj Close'].pct_change()
    stock_data['Volatility'] = stock_data['Daily Return'].rolling(window=30).std()

    # Drop rows with NaN values
    stock_data.dropna(inplace=True)

    return stock_data

dat : pd.DataFrame = preprocess_data(fetch_stock_data("MSFT","2000-01-01","2024-10-06"))

print(dat)