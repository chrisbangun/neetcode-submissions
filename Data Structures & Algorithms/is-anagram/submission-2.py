from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_count = defaultdict(int)
        for char in s:
            s_count[char] += 1
        
        for char in t:
            if char not in s_count:
                return False
            s_count[char] -= 1
            if s_count[char] == 0:
                del s_count[char]
        
        return False if len(s_count) else True