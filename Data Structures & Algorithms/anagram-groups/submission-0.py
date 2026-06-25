from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        
        anagrams = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            anagrams[sorted_word].append(word)

        return [l for l in anagrams.values()]
        