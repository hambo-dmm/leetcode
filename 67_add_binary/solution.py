class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        reversed_a = a[::-1]
        reversed_b = b[::-1]
        
        carry = 0
        iterations = max(len(a), len(b))

        for i in range(iterations):
            # get the values
            a_val = int(reversed_a[i]) if i < len(a) else 0 
            b_val = int(reversed_b[i]) if i < len(b) else 0

            # do the math
            sum = carry + a_val + b_val
            digit = str(sum % 2)
            carry = 1 if sum >= 2 else 0
            result = digit + result
    
        # handle leftover carry
        return result if not carry else str(carry) + result