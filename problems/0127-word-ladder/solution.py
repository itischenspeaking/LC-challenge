class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        visited = set()
        wordList = set(wordList)
        step = 1
        n = len(beginWord)

        q.append((beginWord, step))
        visited.add(beginWord)

        while q:
            cur, step = q.popleft()
            if cur == endWord:
                return step

            for i in range(n):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    nxt = cur[:i] + ch + cur[i+1:]
                    if nxt in wordList and nxt not in visited:
                        q.append((nxt, step+1))
                        visited.add(nxt)

        return 0
