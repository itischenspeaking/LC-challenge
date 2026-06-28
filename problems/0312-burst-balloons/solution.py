# v1: DFS + memo (TLE)
class Solution_DFS:
    def maxCoins(self, nums: list[int]) -> int:
        arr = [1] + nums + [1]
        n = len(arr)
        memo = {}
        def dfs(left, right):
            if right - left == 1:
                return 0
            if (left, right) in memo:
                return memo[(left, right)]
            best = 0
            for k in range(left+1, right):
                coins = dfs(left, k) + arr[left]*arr[k]*arr[right] + dfs(k, right)
                best = max(coins, best)
            memo[(left, right)] = best
            return best
        return dfs(0, n-1)

# v2: Bottom-up DP (accepted)
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        nums = [x for x in nums if x > 0]
        arr = [1] + nums + [1]
        n = len(arr)
        dp = [[0] * n for _ in range(n)]

        for length in range(2, n):
            for left in range(0, n - length):
                right = left + length
                best = 0
                for k in range(left + 1, right):
                    coins = dp[left][k] + arr[left]*arr[k]*arr[right] + dp[k][right]
                    best = max(best, coins)
                dp[left][right] = best

        return dp[0][n - 1]
