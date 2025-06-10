def execute_trade(signal):
    action = signal["action"]
    if action == "buy":
        return "Executed simulated BUY trade"
    elif action == "wait":
        return "Holding position"
    return "No action taken"
