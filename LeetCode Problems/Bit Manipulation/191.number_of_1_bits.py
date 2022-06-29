class Solution:
    def hammingWeight(self, n: int) -> int:
        # brian kernighan algorithm
        set_bits = 0
        while n > 0:
            n &= n - 1
            set_bits += 1
        return set_bits