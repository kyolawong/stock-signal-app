import streamlit as st
import random

st.set_page_config(page_title="Stock Strategy App", layout="wide")

# --- Header ---
st.markdown("<h1 style='text-align: center;'>📈 Stock Strategy Dashboard</h1>", unsafe_allow_html=True)
st.write("Choose your trading horizon from the sidebar and view the signal.")

# Sidebar selection
strategy = st.sidebar.radio(
    "📊 Select Strategy Horizon",
    ["Short-term (Day/Week)", "Mid-term (Weeks/Months)", "Long-term (Months/Years)"]
)

# Fake signals for now
signals = ["Buy", "Sell", "Hold"]
signal = random.choice(signals)

# Layout with two columns
left, right = st.columns([2, 1])

with left:
    if strategy == "Short-term (Day/Week)":
        st.subheader("⚡ Short-term Strategy")
        st.write("For day traders and quick weekly trades.")

    elif strategy == "Mid-term (Weeks/Months)":
        st.subheader("📊 Mid-term Strategy")
        st.write("For swing traders holding for weeks to months.")

    elif strategy == "Long-term (Months/Years)":
        st.subheader("🌱 Long-term Strategy")
        st.write("For investors focused on long horizon trends.")

with right:
    if signal == "Buy":
        st.success("✅ Signal: Buy")
    elif signal == "Sell":
        st.error("❌ Signal: Sell")
    else:
        st.info("➖ Signal: Hold")

# Footer disclaimer
st.markdown("---")
st.caption("⚠️ Disclaimer: Signals are for educational purposes only. Not financial advice.")
