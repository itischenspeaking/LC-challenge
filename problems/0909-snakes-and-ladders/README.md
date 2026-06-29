# 909. Snakes and Ladders

Med | BFS | 2026-06-29

## Approach

BFS from square 1. Each state tries dice rolls 1-6, convert square number to board coordinates, follow snake/ladder if present. First to reach n² wins.

## Complexity

Time: O(n²)  Space: O(n²)

## Notes

- Tricky part is the coordinate conversion: rows alternate direction (boustrophedon)
- BFS guarantees shortest path, no need for DP
