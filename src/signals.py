"""
signals.py
-----------
Placeholder script for generating Mid-Term and Long-Term trading signals.
This is just a blueprint for now.
"""

# Example function for Mid-Term signal
def get_midterm_signal(ticker: str) -> dict:
    return {
        "ticker": ticker,
        "horizon": "midterm",
        "signal": "ADD",        # Example: ADD / HOLD / TRIM
        "score": 72,            # Composite score (0–100)
        "drivers": ["MACD up", "Price > 50MA"]
    }

# Example function for Long-Term signal
def get_longterm_signal(ticker: str) -> dict:
    return {
        "ticker": ticker,
        "horizon": "longterm",
        "signal": "HOLD",
        "score": 85,
        "drivers": ["Strong ROIC", "Low Debt/Equity"]
    }

# Example usage
if __name__ == "__main__":
    print(get_midterm_signal("TSLA"))
    print(get_longterm_signal("MSFT"))
