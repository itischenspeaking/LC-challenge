# 279. Perfect Squares

Med | DP | 2026-06-28

## Approach

BFS-style DP. dp[i] = min squares summing to i. For each i, try subtracting every perfect square.

## Complexity

Time: O(n√n)  Space: O(n)

## Notes

- Same structure as coin change, squares = coins
