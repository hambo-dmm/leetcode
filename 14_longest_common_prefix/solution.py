from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            raise ValueError("No strings provided")
        
        result = strs[0]

        for s in strs[1:]:
            if result == "":
                return result
            result = self._commonPrefix(result, s)

        return result

    def _commonPrefix(self, s, t):
        i = 0
        min_length = min(len(s), len(t))
        while i < min_length and s[i] == t[i]:
            i += 1
        
        return s[:i]