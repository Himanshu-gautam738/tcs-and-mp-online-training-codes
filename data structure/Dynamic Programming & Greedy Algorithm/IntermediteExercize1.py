# Longest Common Subsequence (LCS) using Dynamic Programming

def lcs_length(X, Y):
    m, n = len(X), len(Y)
    # Create a DP table initialized with 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Example usage
X = "ABCAB"
Y = "AECB"
result = lcs_length(X, Y)
print("Length of LCS:", result)
