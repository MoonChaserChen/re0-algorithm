def arr_desc(n: int):
    dp = [""] * (n + 1)
    dp[0] = "1"
    for i in range(1, n + 1):
        v, c = dp[i - 1][0], 1
        for j in range(1, len(dp[i - 1])):
            if dp[i - 1][j] == v:
                c += 1
            else:
                dp[i] += str(c) + v
                v = dp[i - 1][j]
                c = 1
        dp[i] += str(c) + v
    return dp[n]


print(arr_desc(0))
print(arr_desc(1))
print(arr_desc(2))
print(arr_desc(3))
print(arr_desc(4))
print(arr_desc(5))
print(arr_desc(6))
print(arr_desc(7))


