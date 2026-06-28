# 63. Unique Paths II

Med | DP | 2026-06-28

## Approach

Same as 62, but set dp[i][j] = 0 when cell is obstacle.

## Complexity

Time: O(mn)  Space: O(mn)

## Notes

- Obstacle just zeroes out that cell, rest unchanged from #62
