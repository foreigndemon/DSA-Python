class Solution:
    def isHappy(self, n: int) -> bool:
        check_val = set()
        
        while True:
            if n == 1:
                return True
            elif n in check_val:
                return False
            check_val.add(n)
            _sum = 0
            while n:
                _sum += (n%10)**2
                n = n//10
            n = _sum