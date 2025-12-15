class Solution:
    def reverseBits(self, n: int) -> int:
        #return self._reversed_bits_string_manipulation(n)
        return self._reversed_bits_bitwise(n)

    def _reversed_bits_bitwise(self, n):
        result = 0

        for i in range(32):
            bit = (n >> i) & 1

            result |= (bit << (31 -i))

        return result

    def _reversed_bits_string_manipulation(self, n):
        bits = bin(n)[2:]
        padded_bits = bits.zfill(32)
        reversed_padded_bits = padded_bits[::-1]

        return int(reversed_padded_bits, 2)
