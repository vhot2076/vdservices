"""
  Flask http service for get tickers values
"""
import os
from flask import Flask, request, jsonify
from thread_tickers import *
from waitress import serve

# The flask object implements a WSGI application and acts as the central object.
# It is passed the name of the module or package of the application
app = Flask(__name__)


async def get_data_ticker(ticker, start):
    """* Get data from Tickers array"""
    return " ".join(map(str, Tickers[ticker][start:]))


@app.route('/', methods=['GET'])
async def get_ticker():
    """* HTTP GET handler function for tickers request"""
    ticker = request.args.get('ticker', default=0, type=int)
    start = request.args.get('start', default=0, type=int)

    if ticker > 99:
        ticker = 99
    if ticker < 0:
        ticker = 0
    t = await get_data_ticker(ticker, start)
    return jsonify(data=t)

if __name__ == "__main__":
    # Run Flask http service
    serve(app, host=f"{os.getenv('FHOST', '127.0.0.1')}",
          port=f"{os.getenv('FPORT', '5000')}")
