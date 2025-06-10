def generate_trade_signal(market_data):
    pattern = market_data.get("pattern", "none")
    if pattern == "bullish_engulfing":
        return { "action": "buy", "confidence": 0.84 }
    elif pattern == "doji":
        return { "action": "wait", "confidence": 0.55 }
    else:
        return { "action": "hold", "confidence": 0.3 }
