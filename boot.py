from brain.strategist import generate_trade_signal
from signals.patterns import detect_pattern
from body.trader import execute_trade

print("[OBLIVION] Boot sequence initiated...")

candles = [
    {'open': 138.4, 'high': 140.2, 'low': 137.9, 'close': 139.8, 'volume': 820000},
    {'open': 139.7, 'high': 141.3, 'low': 139.0, 'close': 140.9, 'volume': 910000},
]

pattern = detect_pattern(candles)
print("Detected pattern:", pattern)

llm_response = generate_trade_signal(pattern)
print("LLM decision:", llm_response)

result = execute_trade(llm_response)
print("Trade result:", result)
