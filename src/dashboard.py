"""
dashboard.py
-------------
Simple unified interface that combines Mid-Term and Long-Term signals.
"""

from signals import get_midterm_signal, get_longterm_signal

def get_signals_for_watchlist(watchlist: list) -> list:
    results = []
    for ticker in watchlist:
        # Get mid-term signal
        results.append(get_midterm_signal(ticker))
        # Get long-term signal
        results.append(get_longterm_signal(ticker))
    return results

# Example usage
if __name__ == "__main__":
    my_watchlist = ["AAPL", "TSLA", "MSFT"]
    signals = get_signals_for_watchlist(my_watchlist)
    
    print("=== Combined Signals ===")
    for s in signals:
        print(f"{s['ticker']} | {s['horizon'].upper()} | {s['signal']} | Score: {s['score']} | Drivers: {', '.join(s['drivers'])}")
