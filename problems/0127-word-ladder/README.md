# 127. Word Ladder

Hard | BFS | 2026-06-29

## Approach

BFS. For each word, try replacing each character with a-z, check if result is in wordList.

## Complexity

Time: O(n·26·L) where n=wordList size, L=word length  Space: O(n)

## Notes

- Converting wordList to set is key, otherwise lookup kills performance
- Similar pattern to 909: BFS for shortest transformation
