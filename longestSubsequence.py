def lcs(X: str, Y: str):
    m = len(X)
    n = len(Y)

    # Step 1: Create a DP table of size (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Step 2: Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Step 3: Backtrack to find the actual LCS sequence
    i, j = m, n
    lcs_seq = []

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_seq.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    # The sequence is built backwards, so reverse it
    lcs_seq.reverse()

    # Step 4: Return both length and sequence
    return dp[m][n], ''.join(lcs_seq)


X = input('Please enter string 1: ')
Y = input('Please enter string 2: ')
length, sequence = lcs(X, Y)
print(f"LCS length: {length}")
print(f"LCS sequence: {sequence}")
