# strategy.py

def ema_signal(df):
    """
    Returns BUY, SELL or HOLD based on EMA crossover.
    """

    last = df.iloc[-1]
    previous = df.iloc[-2]

    # BUY
    if previous["EMA_9"] < previous["EMA_20"] and last["EMA_9"] > last["EMA_20"]:
        return "BUY"

    # SELL
    if previous["EMA_9"] > previous["EMA_20"] and last["EMA_9"] < last["EMA_20"]:
        return "SELL"

    return "HOLD"
