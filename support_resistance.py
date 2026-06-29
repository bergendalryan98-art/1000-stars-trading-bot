# support_resistance.py

def get_support(df, lookback=20):
    """
    Returns the lowest low over the lookback period.
    """
    return df["low"].tail(lookback).min()


def get_resistance(df, lookback=20):
    """
    Returns the highest high over the lookback period.
    """
    return df["high"].tail(lookback).max()
