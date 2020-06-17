class Solution:
    def findComplement(self, num: int) -> int:
        bits = 0
        n = num
        while n > 0:
            bits += 1
            n = n >> 1
        allBits = 2 ** bits - 1
        return num ^ allBits
