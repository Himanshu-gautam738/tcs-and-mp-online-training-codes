# Coin Change using Greedy Approach

def coin_change_greedy(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    count = 0
    for coin in coins:
        if amount >= coin:
            num = amount // coin      # Take as many of this coin as possible
            count += num
            amount -= num * coin      # Reduce the remaining amount
    return count

# Example usage
coins = [1, 5, 10]
amount = 28
result = coin_change_greedy(coins, amount)
print("Minimum number of coins:", result)
