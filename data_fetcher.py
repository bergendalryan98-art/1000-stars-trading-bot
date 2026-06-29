# data_fetcher.py

import ccxt
import pandas as pd
from config import EXCHANGE


def get_ohlcv(symbol="BTC/USDT", timeframe="5m", limit=200):
    """
    Fetch OHLCV data from the exchange.
    """

    exchange = getattr(ccxt, EXCHANGE)({
        "enableRateLimit": True
    })

    ohlcv = exchange.fetch_ohlcv(symbol, timeframe, limit=limit)

    df = pd.DataFrame(
        ohlcv,
        columns=[
            "timestamp",
            "open",
            "high",
            "low",
            "close",
            "volume",
        ],
    )

    df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")

    return df
