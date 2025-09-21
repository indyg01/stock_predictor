# 📈 Stock Price Predictor

An interactive Streamlit web app that downloads historical stock data from Yahoo Finance, trains a simple machine learning model, and predicts the next day's closing price.

![screenshot](screenshot.png)  <!-- optional screenshot of your app -->

## 🚀 Features
- Download historical data for any stock ticker.
- Compute simple technical indicators (5-day and 20-day moving averages).
- Train a Random Forest model on past data.
- Backtest performance and display RMSE.
- Predict the next day's closing price based on the most recent data.

## 🖥️ Live Demo
[https://your-app-name.streamlit.app](https://your-app-name.streamlit.app) <!-- replace with your deployed link -->

## 🛠️ How to Run Locally

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/stock-predictor.git
cd stock-predictor
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
