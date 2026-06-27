# 343. Integer Break

Med | Math | 2026-06-27

## Approach

Greedily split into 3s. Remainder 1: take back one 3, make 4 (3×1 < 2×2). Remainder 2: just multiply.

## Complexity

Time: O(1)  Space: O(1)

## Notes

- Why 3: maximize (n/x)^x → derivative gives x=e≈2.718, nearest int is 3
- n=2,3 need special cases due to "at least two parts" constraint
