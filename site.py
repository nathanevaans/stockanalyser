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

st.write("""
# Forecaster
""")

container = st.container()
ticker = container.text_input(label='## Stock Ticker').strip()
model = container.selectbox(
        label='## Model',
        options=[
            'None',
            'ARMA',
            'ARIMA',
            'SARIMA',
            'Harmonic Regression'
        ]
    )

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
