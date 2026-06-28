# 62. Unique Paths

Med | DP | 2026-06-28

## Approach

dp[i][j] = dp[i-1][j] + dp[i][j-1]. Pad with zeros to avoid boundary checks.

## Complexity

Time: O(mn)  Space: O(mn)

## Notes

- Could optimize to 1D array since only previous row matters
