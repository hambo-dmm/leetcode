class Solution:
    def hammingWeight(self, n: int) -> int:
        #return self._hamming_weight_string_manipulation(n)
        return self._hamming_weight_bitwise(n)

    def _hamming_weight_bitwise(self, n):
        result = 0
        
        for i in range(32):
            result += 1 if (n >> i) & 1 else 0

        return result

    def _hamming_weight_string_manipulation(self, n):
        bits = bin(n)[2:]
        
        return sum(1 for bit in bits if bit == "1")