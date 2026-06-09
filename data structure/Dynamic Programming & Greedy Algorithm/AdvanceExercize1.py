# Traveling Salesman Problem (TSP) using DP + Bitmasking

def tsp_dp(distance):
    n = len(distance)
    # dp[mask][i] = minimum cost to reach set of cities in mask, ending at city i
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1][0] = 0  # Start at city 0 with mask = 0001

    # Iterate over all subsets of cities
    for mask in range(1 << n):
        for u in range(n):
            if not (mask & (1 << u)):
                continue
            for v in range(n):
                if mask & (1 << v):  # v already visited
                    continue
                new_mask = mask | (1 << v)
                dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + distance[u][v])

    # Return to starting city (0)
    ans = float('inf')
    for u in range(1, n):
        ans = min(ans, dp[(1 << n) - 1][u] + distance[u][0])
    return ans


# Example usage
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

result = tsp_dp(distance_matrix)
print("Minimum TSP route cost:", result)
