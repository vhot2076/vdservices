"""
Data from Flask GET response tickers values
"""
from os import environ
import os
import requests

URL = f"http://{os.getenv('FHOST', '127.0.0.1')}:{os.getenv('FPORT', '5000')}"


def get_data_ticker(ticker, start):
    """Data request function to Flask"""
    response = requests.get(
        URL, params={'ticker': ticker, 'start': start})
    json_data = response.json()
    s = json_data['data']
    return list(map(int, s.split()))
