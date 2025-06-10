def detect_bullish_engulfing(candles):
    if len(candles) < 2:
        return False
    prev = candles[-2]
    curr = candles[-1]
    return (
        prev['close'] < prev['open'] and
        curr['close'] > curr['open'] and
        curr['close'] > prev['open'] and
        curr['open'] < prev['close']
    )

def detect_doji(candle):
    return abs(candle['close'] - candle['open']) < ((candle['high'] - candle['low']) * 0.1)

def detect_pattern(candles):
    results = {}
    if detect_bullish_engulfing(candles):
        results['pattern'] = 'bullish_engulfing'
    elif detect_doji(candles[-1]):
        results['pattern'] = 'doji'
    else:
        results['pattern'] = 'none'
    return results
