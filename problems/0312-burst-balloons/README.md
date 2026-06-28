# 312. Burst Balloons

Hard | DP, Interval | 2026-06-28

## Approach

Interval DP. Think of k as the *last* balloon popped between left and right, so left and right are guaranteed to still exist as boundaries.

## DFS vs DP

Both O(n³) time, but DFS+memo got TLE while bottom-up DP passed. Same complexity, different constant factor:
- Recursion overhead: function call stack per subproblem adds up at n³ scale
- Dict vs array: memo dict hash lookups are slower than dp[i][j] array indexing
- Bottom-up fills in order with no redundant checks, DFS has branching overhead

## Notes

- Filtering out 0s is free optimization — bursting a 0 balloon gives 0 coins
- Key insight: think about which balloon to pop *last*, not first
