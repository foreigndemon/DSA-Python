class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        actual_sum = math.ceil((length * (length + 1))/2)
        summ = 0
        summ = sum(nums)
        return actual_sum - summ