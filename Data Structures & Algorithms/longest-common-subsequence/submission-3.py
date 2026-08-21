class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[-1] * (m + 1) for _ in range (n + 1)]

        def solve(n, m):
            if n == 0 or m == 0:
                return 0

            if dp[n][m] != -1:
                return dp[n][m]

            if text1[n - 1] == text2[m - 1]:
                dp[n][m] = 1 + solve(n - 1, m - 1) 
            else:
                dp[n][m] = max(solve(n - 1, m), solve(n, m - 1))
            return dp[n][m]

        return solve(n, m)

