from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            char_count = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                char_count[idx] += 1
            key = tuple(char_count)
            anagrams[key].append(word)
        
        return list(anagrams.values())
                
        