class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0 
        max_len = 0
        visited = set()

        while right < len(s):
            if s[right] not in visited:
                visited.add(s[right])
                max_len = max(max_len, right - left + 1)
                right = right + 1
            else:
                visited.remove(s[left])
                left = left + 1
        return max_len