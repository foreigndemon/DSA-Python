class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = {}
        for num in nums:
            hash[num] =True
        
        for num in nums:
            if num - 1 in hash:
                hash[num] = False
        
        maxLen = 0
        for num in nums:
            if hash.get(num) == True:
                length = 1
                
                while True:
                    num += 1
                    if num not in hash:
                        break
                    length += 1
                
                maxLen = max(maxLen,length)
        return maxLen
                
                
                
        
        