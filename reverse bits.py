class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            # Extract the i-th bit from n
            bit = (n >> i) & 1
            # Place the extracted bit at the (31 - i)-th position in res
            res = res | (bit << (31 - i))
        return res
