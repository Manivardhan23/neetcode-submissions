class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = []
        def backtracking(start_index, current_path):
            if sum(current_path) == target:
                answer.append(current_path.copy())
                return
            if sum(current_path) > target:
                return 

            for i in range (start_index, len(nums)):
                current_path.append(nums[i])
                backtracking(i, current_path)
                current_path.pop()
        backtracking(0, [])
        return answer 

