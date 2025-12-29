PROJECT = {
    "name": "Portfolio Optimization",
    "icon": "💼",
    "dataset": "Historical Stock Data",
    "description": "Optimize investment weights using Modern Portfolio Theory.",
    "steps": "Fetch → Returns → Efficient frontier",
    "code": """
import yfinance as yf
from pypfopt import EfficientFrontier, risk_models, expected_returns

tickers = ["AAPL", "MSFT", "GOOG", "AMZN"]
df = yf.download(tickers, period="5y")["Close"]

mu = expected_returns.mean_historical_return(df)
S = risk_models.sample_cov(df)

ef = EfficientFrontier(mu, S)
weights = ef.max_sharpe()
cleaned = ef.clean_weights()

print(cleaned)
"""
}
