# 64. Minimum Path Sum

Med | DP | 2026-06-28

## Approach

dp[i][j] = grid value + min(left, top). Pad with inf, seed dp[1][0]=0.

## Complexity

Time: O(mn)  Space: O(mn)

## Notes

- Same grid DP pattern as 62/63, just min instead of sum
