class Solution:
    def rob(self, nums: List[int]) -> int:
        def solve(new_nums):
            n = len(new_nums)
            dp = [0] * (n + 1)
            dp[1] = new_nums[0]
            for i in range (2, n + 1):
                dp[i] = max(dp[i - 1], new_nums[i - 1] + dp[i - 2])

            return dp[n]

        length = len(nums)
        if length == 1:
            return nums[0]
        ans = max(solve(nums[ : length - 1]), solve(nums[1 : ]))
        return ans