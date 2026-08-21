class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[-1] * (m + 1) for _ in range(n + 1)]

        def solve(i, j):
            if i == 0 or j == 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = 1 + solve(i - 1, j - 1)
            else:
                dp[i][j] = max(solve(i - 1, j), solve(i, j - 1))
            
            return dp[i][j]

        return solve(n, m)
