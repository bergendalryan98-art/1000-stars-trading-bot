# indicators.py

import pandas as pd


def calculate_ema(df, period):
    """
    Calculate an Exponential Moving Average (EMA).
    """
    return df["close"].ewm(span=period, adjust=False).mean()


def add_indicators(df):
    """
    Add all trading indicators to the DataFrame.
    """

    # EMA 9
    df["EMA_9"] = calculate_ema(df, 9)

    # EMA 20
    df["EMA_20"] = calculate_ema(df, 20)

    return df
