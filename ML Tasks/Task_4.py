import pandas as pd
import datetime as dt
from datetime import date
import matplotlib.pyplot as plt
import yfinance as yf
import numpy as np
import tensorflow as tf
from sklearn.model_selection import train_test_split
from tensorflow.keras.layers import Dense, Dropout, LSTM, Input
from tensorflow.keras.models import Sequential
import matplotlib.dates as mdates

START = "2010-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

# Function to load the dataset
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

data = load_data('TCS.NS')
df = data

# Set Date as index
df.set_index('Date', inplace=True)

# Drop unnecessary columns for display
print(df.drop(['Open', 'High', 'Low', 'Adj Close', 'Volume'], axis=1).head(5))

plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price')

# Format the x-axis to show dates
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

plt.title("TCS Stock Price")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.grid(True)
plt.legend()
plt.xticks(rotation=45)
plt.show()
