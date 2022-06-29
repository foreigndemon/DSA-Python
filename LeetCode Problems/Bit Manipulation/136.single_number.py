class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor operator
        res = 0
        for num in nums:
            res = num ^ res
        return res
    
        
        # other one way to do it!
        # hash = {}
        # for num in nums:
        #     if num not in hash:
        #         hash[num] = 1
        #     else:
        #         hash[num] += 1
        # for key,val in hash.items():
        #     if val == 1:
        #         return key