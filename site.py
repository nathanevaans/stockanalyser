import streamlit as st
import pandas as pd
import numpy as np

tickers = {
    'AAPL': 'Apple Inc.',
    'MSFT': 'Microsoft Corporation',
    'GOOG': 'Alphabet Inc. Class C',
    'GOOGL': 'Alphabet Inc. Class A',
    'AMZN': 'Amazon.com, Inc.',
    'NVDA': 'NVIDIA Corporation',
    'BRK/A': 'Berkshire Hathaway Inc.',
    'META': 'Meta Platforms, Inc. Class A',
    'BRK/B': 'Berkshire Hathaway Inc.',
    'TSLA': 'Tesla, Inc.'
}

exchanges = {
    "NYSE": {"name": "New York Stock Exchange", "location": "USA"},
    "NASDAQ": {"name": "NASDAQ", "location": "USA"},
    "TSE": {"name": "Tokyo Stock Exchange", "location": "Japan"},
    "SSE": {"name": "Shanghai Stock Exchange", "location": "China"},
    "HKEX": {"name": "Hong Kong Stock Exchange", "location": "Hong Kong"},
    "Euronext": {"name": "Euronext", "location": "Europe"},
    "LSE": {"name": "London Stock Exchange", "location": "UK"},
    "SZSE": {"name": "Shenzhen Stock Exchange", "location": "China"},
    "TSX": {"name": "Toronto Stock Exchange", "location": "Canada"},
    "FWB": {"name": "Frankfurt Stock Exchange", "location": "Germany"}
}

st.write("""
# Forecaster
""")

container = st.container()
exchange = container.selectbox(
    label='Exchange',
    options=['Select an Exchange'] + [key for key in exchanges.keys()]
)
ticker = container.text_input(label='Stock Ticker').strip()
model = container.selectbox(
        label='Model',
        options=[
            'None',
            'ARMA',
            'ARIMA',
            'SARIMA',
            'Harmonic Regression',
            'Fourier Analysis'
        ]
    )

# create a dictionary of exchanges that contain records of tickers and stuff
if exchange != 'Select an Exchange':
    if ticker == '':
        st.write('')
    elif ticker not in tickers:
        st.error("Ticker not available")
    else:
        st.success(tickers[ticker])
        if model != 'None':
            # do logic and alter graph
            forecast_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
            st.line_chart(forecast_data, use_container_width=True)
        else:
            # un edtited graph
            forecast_data = pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
            st.line_chart(forecast_data, use_container_width=True)

# perhaps use a form to with text input and two select boxes and once all done you press forecast button
