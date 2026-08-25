class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for num in num_set:
            if num - 1 in num_set:
                continue

            curr = num
            length = 1

            while curr + 1 in num_set:
                curr += 1
                length += 1

            longest = max(longest, length)

        return longest