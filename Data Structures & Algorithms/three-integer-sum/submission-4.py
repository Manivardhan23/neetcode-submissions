class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        sort_nums = sorted(nums)
        for i in range(len(nums)):
            if i > 0 and sort_nums[i] == sort_nums[i - 1]:
                continue
            target = -(sort_nums[i])
            left = i + 1
            right = len(nums) - 1
            while (left < right):
                if sort_nums[left] + sort_nums[right] == target:
                    answer.append([sort_nums[i], sort_nums[left], sort_nums[right]])
                    left += 1
                    right -= 1
                    while left < right and sort_nums[left] == sort_nums[left - 1]:
                        left += 1
                    while left < right and sort_nums[right] == sort_nums[right + 1]:
                        right -= 1
                elif sort_nums[left] + sort_nums[right] < target:
                    left += 1
                else:
                    right -= 1
        return answer