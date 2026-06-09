# Dynamic Programming Solution (Guaranteed Optimal)
def coin_change_dp(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0 

    # Build DP table
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Sort coins descending
    count = 0
    for coin in coins:
        if amount >= coin:
            num = amount // coin
            count += num
            amount -= num * coin
    return count if amount == 0 else -1


coins = [1, 5, 10, 25]   # Example coin denominations
amount = 63              # Example target amount

print("Coin denominations:", coins)
print("Target amount:", amount)

# Dynamic Programming Result
dp_result = coin_change_dp(coins, amount)
print("DP Solution - Minimum coins:", dp_result)

# Greedy Result
greedy_result = coin_change_greedy(coins, amount)
print("Greedy Solution - Minimum coins:", greedy_result)
