class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        target = n*n
        
        def get_pos(num_cur):
            a = (num_cur-1)//n
            b = (num_cur-1)%n

            if a%2 == 0:
                r = n-a-1
                c = b
            else:
                r = n-a-1
                c = n-b-1

            return r, c

        q = deque()
        q.append((1,0))
        
        visited = set()
        visited.add(1)

        while q:
            cur, step = q.popleft()

            if cur == target:
                return step

            for i in range(1, 7):
                nxt = cur + i
                if nxt > target:
                    continue
                
                r, c = get_pos(nxt)
                
                if board[r][c] != -1:
                    nxt = board[r][c]
                
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, step+1))

        return -1
