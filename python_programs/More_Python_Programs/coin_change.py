def minimum_coins(coins, amount):
                                                                       
    if amount < 0 or any(coin <= 0 for coin in coins):
        raise ValueError("amount must be non-negative and coins positive")
    dp = [0] + [float("inf")] * amount
    for current in range(1, amount + 1):
        dp[current] = min((dp[current - coin] + 1 for coin in coins if coin <= current), default=float("inf"))
    return None if dp[amount] == float("inf") else dp[amount]

if __name__ == "__main__":
    print(minimum_coins([1, 3, 4], 6))
