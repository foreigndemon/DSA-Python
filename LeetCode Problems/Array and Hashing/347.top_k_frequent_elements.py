class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_hash = {}
        freq_list = [[] for i in range(len(nums)+1)]
        
        for num in nums:
            if num not in freq_hash:
                freq_hash[num] = 1
            else:
                freq_hash[num] += 1
                
        for key, val in freq_hash.items():
            freq_list[val].append(key)
        
        
        result = []
        for i in range(len(freq_list)-1,0,-1):
            for num in freq_list[i]:
                result.append(num)
                if len(result) == k:
                    return result
                
            
            