import streamlit as st
import yfinance as yf
import pandas as pd

st.set_page_config(page_title="Stock Strategy App", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>📈 Stock Strategy Dashboard</h1>", unsafe_allow_html=True)
st.write("Choose your trading horizon from the sidebar, enter a stock ticker, and view the signal.")

# Sidebar selection
strategy = st.sidebar.radio(
    "📊 Select Strategy Horizon",
    ["Short-term (Day/Week)", "Mid-term (Weeks/Months)", "Long-term (Months/Years)"]
)

# --- Stock ticker input ---
ticker = st.text_input("🔎 Enter Stock Ticker (e.g., AAPL, TSLA, MSFT):", value="AAPL").upper()

def generate_signal(ticker, strategy):
    try:
        if strategy == "Short-term (Day/Week)":
            data = yf.download(ticker, period="5d", interval="1d")
        elif strategy == "Mid-term (Weeks/Months)":
            data = yf.download(ticker, period="1mo", interval="1d")
        else:
            data = yf.download(ticker, period="6mo", interval="1d")

        if data.empty:
            return "No Data"

        last_price = float(data["Close"].iloc[-1])
        first_price = float(data["Close"].iloc[0])
        change = ((last_price - first_price) / first_price) * 100.0

        if change > 2:
            return f"Buy (Up {change:.2f}%)"
        elif change < -2:
            return f"Sell (Down {change:.2f}%)"
        else:
            return f"Hold (Change {change:.2f}%)"

    except Exception as e:
        return f"Error: {str(e)}"


signal = generate_signal(ticker, strategy)

# Layout with two columns
left, right = st.columns([2, 1])

with left:
    if strategy == "Short-term (Day/Week)":
        st.subheader(f"⚡ Short-term Strategy for {ticker}")
        st.write("Based on the past 5 trading days.")

    elif strategy == "Mid-term (Weeks/Months)":
        st.subheader(f"📊 Mid-term Strategy for {ticker}")
        st.write("Based on the past 1 month trend.")

    elif strategy == "Long-term (Months/Years)":
        st.subheader(f"🌱 Long-term Strategy for {ticker}")
        st.write("Based on the past 6 months trend.")

with right:
    if "Buy" in signal:
        st.success(f"✅ Signal for {ticker}: {signal}")
    elif "Sell" in signal:
        st.error(f"❌ Signal for {ticker}: {signal}")
    elif "Hold" in signal:
        st.info(f"➖ Signal for {ticker}: {signal}")
    else:
        st.warning(signal)

# Footer disclaimer
st.markdown("---")
st.caption("⚠️ Disclaimer: Signals are for educational purposes only. Not financial advice.")
