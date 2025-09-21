import streamlit as st
import yfinance as yf
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

st.title("Tomorrow Price")

# User input for stock ticker
ticker = st.text_input("Ticker?", "NVDA")
start_date = st.date_input("Start date", pd.to_datetime("2020-01-01"))
end_date = st.date_input("End date", pd.to_datetime("2025-01-01"))

if st.button("Predict"):
    # Fetch historical data
    data = yf.download(ticker, start=start_date, end=end_date)

    if data.empty:
        st.error("No data found for the given ticker and date range.")
    else:
        # Target: Tomorrows close price
        close = data['Close']
        tomorrow_close = close.shift(-1)

        data['Tomorrow'] = tomorrow_close

        # --- Features ---
        data['SMA_5'] = data['Close'].rolling(5).mean()
        data['SMA_20'] = data['Close'].rolling(20).mean()
        data = data.dropna()

        features = ['SMA_5', 'SMA_20']
        X = data[features]
        y = data['Tomorrow']  # predict tomorrow's price directly

        # --- Split (80% train, 20% test) ---
        split = int(len(X) * 0.8)
        X_train, X_test = X[:split], X[split:]
        y_train, y_test = y[:split], y[split:]

        # --- Model ---
        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, preds))

        # Show backtest RSME
        st.subheader(f"Backtest RMSE on last {len(y_test)} days: {rmse:.2f}")
        st.line_chart(
            pd.DataFrame({"Actual Price": y_test.values, "Predicted Price": preds}, index=y_test.index)
        )

        # --- Predict tomorrow's price ---
        latest_features = X.iloc[-1:].values  # most recent row of features
        tomorrow_price_pred = model.predict(latest_features)[0]

        st.success(f"Model's guess for the next day's closing price: ${tomorrow_price_pred:.2f}")