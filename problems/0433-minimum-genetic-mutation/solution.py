class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        q = deque()
        visited = set()

        q.append((startGene, 0))
        visited.add(startGene)
        Avail = ['A', 'C', 'G', 'T']

        while q:
            cur, step = q.popleft()
            if cur == endGene:
                return step

            for i in range(8):
                for ch in Avail:
                    nxt = cur[:i] + ch + cur[i+1:]

                    if nxt in bank and nxt not in visited:
                        q.append((nxt, step+1))
                        visited.add(nxt)

        return -1
