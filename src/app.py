import streamlit as st
import random

st.set_page_config(page_title="Stock Strategy App", layout="wide")

st.title("📈 Stock Strategy App")
st.write("Choose your preferred trading horizon and get a signal.")

# Sidebar selection
strategy = st.sidebar.radio(
    "Select Strategy",
    ["Short-term (Day/Week)", "Mid-term (Weeks/Months)", "Long-term (Months/Years)"]
)

# Fake signals for now (we’ll later connect to real stock data)
signals = ["Buy", "Sell", "Hold"]

if strategy == "Short-term (Day/Week)":
    st.subheader("⚡ Short-term Strategy")
    st.write("Designed for day traders and quick weekly trades.")
    st.success(f"Signal: {random.choice(signals)}")

elif strategy == "Mid-term (Weeks/Months)":
    st.subheader("📊 Mid-term Strategy")
    st.write("Designed for swing traders holding for weeks to months.")
    st.info(f"Signal: {random.choice(signals)}")

elif strategy == "Long-term (Months/Years)":
    st.subheader("🌱 Long-term Strategy")
    st.write("Designed for investors focused on long horizon trends.")
    st.warning(f"Signal: {random.choice(signals)}")
