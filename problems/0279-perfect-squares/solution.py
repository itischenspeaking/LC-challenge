class Solution:
    def numSquares(self, n: int) -> int:
        cap = int(n**(1/2))
        sqrs = [i**2 for i in range(1, cap+1)]
        dp = [float("inf")]* (n+1)
        dp[0] = 0
        dp[1] = 1
        for i in range(2, n+1):
            for sqr in sqrs:
                if i - sqr >= 0:
                    dp[i] = min(dp[i], dp[i-sqr] +1)

        return dp[n]
