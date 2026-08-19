class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        d = [(1,0), (-1,0), (0, 1), (0, -1)]  
        R = len(board)
        C = len(board[0])

        def dfs(r, c, k):
            if r < 0 or r >= R or c < 0 or c >= C:
                return False 
            if board[r][c] != word[k]:
                return False
            if k == len(word) - 1:
                return True

            temp = board[r][c]
            board[r][c] = "#" 
            for dr, dc in d:
                if dfs(r + dr, c + dc, k + 1):
                    board[r][c] = temp
                    return True
            board[r][c] = temp
            return False

        for i in range(R):
            for j in range(C):
                if dfs(i, j, 0):
                    return True
        return False