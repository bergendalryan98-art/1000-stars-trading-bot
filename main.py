
# main.py

from data_fetcher import get_ohlcv
from indicators import add_indicators
from strategy import ema_signal
from support_resistance import get_support, get_resistance


def main():
    print("=" * 50)
    print("      1000 STARS TRADING BOT")
    print("=" * 50)

    # Download market data
    df = get_ohlcv(
        symbol="BTC/USDT",
        timeframe="5m",
        limit=200
    )

    # Calculate indicators
    df = add_indicators(df)

    # Trading signal
    signal = ema_signal(df)

    # Support & Resistance
    support = get_support(df)
    resistance = get_resistance(df)

    # Latest price
    price = df.iloc[-1]["close"]

    print(f"Current Price : {price:.2f}")
    print(f"EMA Signal    : {signal}")
    print(f"Support       : {support:.2f}")
    print(f"Resistance    : {resistance:.2f}")

    print("=" * 50)


if __name__ == "__main__":
    main()
