class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s, hash_t = {}, {}
        for val in s:
            if val not in hash_s:
                hash_s[val] = 1
            else:
                hash_s[val] += 1                
        for val in t:
            if val not in hash_t:
                hash_t[val] = 1
            else:
                hash_t[val] += 1
                
        if hash_s == hash_t:
            return True
        else:
            False
        