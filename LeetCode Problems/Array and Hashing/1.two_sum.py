class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, val in enumerate(nums):
            if val not in hash:
                hash[target-val] = idx
            else:
                return [idx,hash[val]]
