# 994. Rotting Oranges

Med | BFS | 2026-06-30

## Approach

Multi-source BFS. Enqueue all rotten oranges at step 0, spread outward. Check for remaining fresh at the end.

## Complexity

Time: O(mn)  Space: O(mn)

## Notes

- Classic multi-source BFS — start from all sources simultaneously
- Mutating grid in-place doubles as visited check
