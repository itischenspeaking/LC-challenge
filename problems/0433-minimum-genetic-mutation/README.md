# 433. Minimum Genetic Mutation

Med | BFS | 2026-06-29

## Approach

BFS. For each position (8 chars), try all 4 possible mutations. Only enqueue if result is in bank.

## Complexity

Time: O(8×4×n) where n = bank size  Space: O(n)

## Notes

- Essentially same pattern as 909 and word ladder: BFS on implicit graph
- Bank acts as both adjacency filter and visited bound
