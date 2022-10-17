"""
  Thread daemon for generate tickers values
"""

from random import random
import time
import threading

# Array of arrays of values for all tickers
Tickers = [[0] for i in range(100)]


def generate_movement():
    """Generate virtual value function"""
    movement = -1 if random() < 0.5 else 1
    return movement


def add_tickers():
    """Add virtual values for all tickers procedure"""
    while True:
        t1 = time.perf_counter()
        for i in Tickers:
            i.append(i[-1] + generate_movement())
        t2 = time.perf_counter()
        # Create time delay about 1 sec
        time.sleep(1-t2+t1)


# Emulating a subset of Java's threading model.
threading.Thread(target=add_tickers, daemon=True).start()
