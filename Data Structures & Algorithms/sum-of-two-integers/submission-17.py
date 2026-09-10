class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxVal = 0x7FFFFFFF

        while b:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask
        
        return a if a <= maxVal else ~(a ^ mask)