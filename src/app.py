"""
app.py
-------
Streamlit web app that displays Mid-Term and Long-Term signals together.
"""

import streamlit as st
from signals import get_midterm_signal, get_longterm_signal

st.set_page_config(page_title="Stock Signal Dashboard", layout="wide")

st.title("📊 Stock Signal Dashboard")
st.write("Mid-Term and Long-Term signals in one place")

# Watchlist input
tickers = st.text_input("Enter stock tickers (comma separated):", "AAPL, TSLA, MSFT")
watchlist = [t.strip().upper() for t in tickers.split(",") if t.strip()]

# Generate signals
signals = []
for ticker in watchlist:
    signals.append(get_midterm_signal(ticker))
    signals.append(get_longterm_signal(ticker))

# Display signals in a table
if signals:
    st.subheader("Combined Signals")
    st.table(signals)
else:
    st.info("Enter at least one ticker to see signals.")
