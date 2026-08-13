class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 1
        right = len(numbers)
        for i in range (1, len(numbers) + 1):
            if (numbers[left - 1] + numbers[right - 1]) == target:
                return [left, right]

            if (numbers[left - 1] + numbers[right - 1]) < target:
                left += 1
            else:
                right -= 1
        return -1